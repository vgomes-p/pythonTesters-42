# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    module2.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/12 14:55:15 by vigomes-          #+#    #+#              #
#    Updated: 2026/09/03 19:19:43 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout
import time as tm
import argparse
import os
import subprocess

DEFAULT = "\033[m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YLOW = "\033[1;33m"
PINK = "\033[1;35m"
CYAN = "\033[1;36m"
INVERT = "\033[1;4;7;97m"
BOLD = "\033[1m"

ep0 = {
    0: "Input data is '25'\nTemperature is now 25°C\n\n",
    1: "Input data is 'abc'\nCaught input_temperature value error: entry 'abc' is not valid for int() convertion\n\n",
    2: "Input data is '42'\nTemperature is now 42°C\n\n",
    3: "Input data is '-51'\nTemperature is now -51°C\n\n",
    4: "Input data is '42sp'\nCaught input_temperature value error: entry '42sp' is not valid for int() convertion\n\n",
    }

ep1 = {
    0: "Input data is '25'\nTemperature is now 25°C\n\n",
    1: "Input data is 'abc'\nCaught input_temperature value error: entry 'abc' is not valid for int() convertion\n\n",
    2: "Input data is '42'\nCaught input_temperature warning: temperature warning: 42°C is too hot for plant(max 40°C)\n\n",
    3: "Input data is '-51'\nCaught input_temperature warning: temperature warning: -51°C is too cold for plant(min 0°C)\n\n",
    4: "Input data is '42sp'\nCaught input_temperature value error: entry '42sp' is not valid for int() convertion\n\n",
    }

ep2 = {
    0: "Testing operation 0...\nCaught ValueError: invalid literal for int() with base 10: 'abc'\n",
    1: "Testing operation 1...\nCaught ZeroDivisionError: division by zero\n",
    2: "Testing operation 2...\nCaught FileNotFoundError: [Errno 2] No such file or directory: '/non/existent/file'\n",
    3: "Testing operation 3...\nCaught TypeError: can only concatenate str (not \"int\") to str\n",
    4: "Testing operation 4...\n",
    }

ep3 = {
    0: "Testing 0...\n>> done\n",
    1: "Testing 1...\n>> Caught GardenError: Garden name can only contain letters\n",
    2: "Testing 2...\n>> Caught GardenError: Garden name can only contain letters\n",
    3: "Testing 3...\n>> done\n",
    4: "Testing 4...\n>> Caught PlantError: '5unFl0ower' is invalid! Plant name can only be alphabetic\n",
    5: "Testing 5...\n>> Caught PlantError: '42' is invalid! Plant name can only be alphabetic\n",
    6: "Testing 6...\n>> done\n",
    7: "Testing 7...\n>> Caught PlantError: Age for plant Cactus is invalid! Plant age cannot be negative\n",
    8: "Testing 8...\n>> done\n",
    9: "Testing 9...\n>> Caught WaterError: Last time watered cannot be negative!\n",
    10: "All custom error types work correctly!\n",
    }

ep4 = {
    0: "Watering Tomato: [OK]\nClosing watering system...\n",
    1: "Watering Lettuce: [OK]\nClosing watering system...\n",
    2: "Watering Carrots: [OK]\nClosing watering system...\n",
    3: "Watering waterMellon: Caught WaterError: Invalid plant name to water: 'waterMellon'\n... ending tests and returing to main\nClosing watering system...\n",
    4: "Cleanup always happens, even with errors!\n",
    }


def clear() -> None:
    cmd = []
    os_name = os.name
    if os_name == "nt":
        cmd.append("cls")
    else:
        cmd.append("clear")
    try:
        subprocess.run(cmd)
    except Exception as e:
        pass


def printnl(times: int=0) -> None:
    print("\n" * times, end="")


def error_message(error: str, x: bool=True) -> None:
    if (x):
        print("❌", end='')
    print(f"{RED} {error}{DEFAULT}")


def biggest_name(dict_names: dict) -> int:
    biggest = 0
    for code in dict_names:
        name_len = len(dict_names[code])
        if name_len >= biggest:
            biggest = name_len
    return biggest


auto_final_text_s = "CONGRATS, ALL RAN SUCESSFULLY!"
auto_final_text_f = "SOMETHING IS WRONG, REVIEW YOUR CODE!"
CAUTION_MESSAGE0 = RED + "\nCaution: " + YLOW + """for this exercise, the tester do not check or test the function
that test the yours custom raised classes as requested on subject,
it tests all the classes. So, be sure to create and test
the your own teste 'test_personal_errors_type()'""" + DEFAULT
CAUTION_MESSAGE1 = RED + "\nCaution: " + YLOW + """for this exercise, the tester do not check or test the 'test_watering_system'
requested on subject, it tests the 'water_plant' raised value. Be sure to test
the test_watering_system on your own""" + DEFAULT


def get_class_name(target) -> str:
    try:
        name = target.__class__.__name__
    except TypeError as e:
        name = f"Type error: {e} | expected class type"
    except Exception as e:
        name = f"{e.__class__.__name__}: {e}"
    return name


# EX0 -- ft_first_exception.py
def test_temperature0(function, inp) -> None:
    print(f"Input data is '{inp}'")
    try:
        temp = function(inp)
        print(f"Temperature is now {temp}°C", end="\n\n")
    except ValueError as e:
        print(f"Caught input_temperature value error: {e}", end="\n\n")
    except Exception as e:
        print(f"Caught input_temperature warning: {e}", end="\n\n")


# EX1 -- ft_raise_exception.py
def test_temperature1(function, inp) -> None:

    print(f"Input data is '{inp}'")
    try:
        temp = function(inp)
        print(f"Temperature is now {temp}°C", end="\n\n")
    except ValueError as e:
        print(f"Caught input_temperature value error: {e}", end="\n\n")
    except Exception as e:
        print(f"Caught input_temperature warning: {e}", end="\n\n")


# EX2 -- ft_different_errors.py
def test_error_types(function, op) -> None:
    print(f"Testing operation {op}...")
    try:
        function(op)
    except Exception as e:
        exception_type = str(e.__class__.__name__)
        print(f"Caught {exception_type}: {e}")


# EX3 -- ft_custom_errors.py
def test_class_name(c, expected: str) -> None:
    if c.__class__.__name__ == expected:
        print('✅', end='')
        return
    print('❌', end='')

def test_personal_errors_type(GardenError, PlantError, WaterError,
                              testing: dict, test_number: int) -> None:
    def thereis_number(entry: str) -> bool:
        for c in entry:
            if c.isnumeric():
                return True
        return False

    def validate_garden(garden_name: str) -> bool:
        if thereis_number(garden_name):
            raise GardenError("Garden name can only contain letters")
        elif garden_name.isnumeric():
            raise GardenError("Garden name cannot be integer")
        else:
            return True

    def validate_plant(plant_name: str, plant_age: int) -> bool:
        if thereis_number(plant_name):
            raise PlantError(f"'{plant_name}' is invalid!" +
                            " Plant name can only be alphabetic")
        elif plant_name.isnumeric():
            raise PlantError(f"'{plant_name}' is invalid!" +
                            " Plant name cannot be integer")
        elif plant_age < 0:
            raise PlantError(f"Age for plant {plant_name} is invalid!" +
                            " Plant age cannot be negative")
        else:
            return True

    def validate_watering(last_time_watered: int) -> bool:
        if last_time_watered < 0:
            raise WaterError("Last time watered cannot be negative!")
        if last_time_watered > 3:
            return True
        else:
            return False

    print(f"Testing {test_number}...")
    # print(testing)
    func = testing.get("function")
    params = testing.get("params")
    # print(params)
    try:
        match func:
            case "validate_garden":
                # print("get to validate garden one param")
                # print(f"param: {params[0]}")
                validate_garden(params[0])
            case "validate_plant":
                # print("get to validate plant one param")
                # print(f"param: {params[0], params[1]}")
                validate_plant(params[0], params[1])
            case "validate_watering":
                # print("get to validate watering one param")
                # print(f"param: {params[0]}")
                validate_watering(params[0])
        print(">> done")
    except Exception as e:
        error_type = e.__class__.__name__
        print(f">> Caught {error_type}: {e}")


# EX4 -- ft_finally_block.py
def test_watering_system(function, param: str) -> str:
    try:
        print(f"Watering {param}: ", end="")
        function(param)
    except Exception as e:
        error_type = e.__class__.__name__
        print(f"Caught {error_type}: {e}")
        print("... ending tests and returing to main")
    finally:
        print("Closing watering system...")
        return "clear"

def main_watering_system(function):
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    ret = test_watering_system(function)
    if ret == "clear":
        print("\nCleanup always happens, even with errors!")
    else:
        print("\nCleanup failed!")


def exec_unit_test(function, tester, function_name: str, parameters: list,
                   expected: dict, space_time: int = 1,
                   view: bool = False, time: float = 0.5) -> tuple[int, int]:
    stats = 0
    print(
        f"{CYAN}\n{function_name}:{' ' * space_time}{DEFAULT}",
        end=('\n' if view else ''),
        flush=True
    )
    i = 0
    for parameter in parameters:
        tm.sleep(time)
        expect = expected[i]
        buffer = StringIO()
        try:
            with redirect_stdout(buffer):
                tester(function, parameter)
            output = buffer.getvalue()
            if output == expect:
                print('✅', end='', flush=True)
            else:
                print('❌', end='', flush=True)
                stats = 1
            if view:
                print(f"\nEXPECTED:\n{expect}\nOUTPUT:\n{output}")
        except Exception as e:
            error_message(
                f"Serious error on running {function_name}(): {e}"
            )
            return 1, 1
        i += 1
    printnl()
    return 0, stats


def exec_unit_class_test0(tester, class1, class2, class3,
                          function_name: str, parameters: dict,
                          expected: dict, space_time: int = 1,
                          view: bool = False, time: float = 0.5
                          ) -> tuple[int, int]:
    stats = 0
    if time == 0.5 and view == False:
        print(CAUTION_MESSAGE0, end='')
    print(
        f"\n{CYAN}{function_name}:{' ' * space_time}{DEFAULT}",
        end=('\n' if view else ''),
        flush=True
    )
    for i in range(0, 11):
        tm.sleep(time)
        expect = expected[i]
        buffer = StringIO()
        try:
            with redirect_stdout(buffer):
                if i == 10:
                    success = "All custom error types work correctly!"
                    failed = "Something went wrong!"
                    print(success if stats == 0 else failed)
                else:
                    tester(class1, class2, class3, parameters[i], i)
            output = buffer.getvalue()
            if output == expect:
                print('✅', end='', flush=True)
            else:
                print('❌', end='', flush=True)
                stats = 1
            if view:
                print(f"\nEXPECTED:\n{expect}\nOUTPUT:\n{output}")
        except Exception as e:
            error_message(
                f"Serious error on running {function_name}(): {e}"
            )
            return 1, 1
    printnl()
    return 0, stats

def exec_unit_class_test1(tester, function, function_name: str,
                          parameters: list, expected: dict,
                          space_time: int = 1, view: bool = False,
                          time: float = 0.5) -> tuple[int, int]:
    stats = 0
    if time == 0.5 and view == False:
        print(CAUTION_MESSAGE1, end='')
    print(
        f"\n{CYAN}{function_name}:{' ' * space_time}{DEFAULT}",
        end=('\n' if view else ''),
        flush=True
    )
    clear = 0
    for i in range(0, 5):
        tm.sleep(time)
        if i < 4:
            parameter = parameters[i]
        expect = expected[i]
        buffer = StringIO()
        try:
            with redirect_stdout(buffer):
                if i == 4:
                    success = "Cleanup always happens, even with errors!"
                    failed = "Cleanup failed!"
                    print(success if clear == 4 else failed)
                else:
                    ret = tester(function, parameter)
            output = buffer.getvalue()
            if ret == "clear":
                clear += 1
            if output == expect:
                print('✅', end='', flush=True)
            else:
                print('❌', end='', flush=True)
                stats = 1
            if view:
                print(f"\nEXPECTED:\n{expect}\nOUTPUT:\n{output}")
        except Exception as e:
            error_message(
                f"Serious error on running {function_name}(): {e}"
            )
            return 1, 1
    printnl()
    return 0, stats


def exec_tests(view: bool, time: float) -> int:
    try:
        from ex0.ft_first_exception import input_temperature as it0
        from ex1.ft_raise_exception import input_temperature as it1
        from ex2.ft_different_errors import garden_operations
        from ex3.ft_custom_errors import PlantError, WaterError, GardenError
        from ex4.ft_finally_block import water_plant
    except ImportError as e:
        error_message(e)
    finally:
        funcs = {
            "f0": [it0, test_temperature0],
            "f1": [it1, test_temperature1],
            "f2": [garden_operations, test_error_types],
            "f3": [GardenError, PlantError, WaterError,
                   test_personal_errors_type],
            "f4": [water_plant, test_watering_system],
        }

        fp3_test = {
            0: {"function": "validate_garden", "params": ["My Litte garden"]},
            1: {"function": "validate_garden", "params": ["4 b1g gard3n"]},
            2: {"function": "validate_garden", "params": ["42"]},
            3: {"function": "validate_plant", "params": ["Cactus", 42]},
            4: {"function": "validate_plant", "params": ["5unFl0ower", 4]},
            5: {"function": "validate_plant", "params": ["42", 52]},
            6: {"function": "validate_plant", "params": ["Cactus", 0]},
            7: {"function": "validate_plant", "params": ["Cactus", -365]},
            8: {"function": "validate_watering", "params": [42]},
            9: {"function": "validate_watering", "params": [-42]}
        }

        funcs_params = {
            "f0": ["25", "abc", "42", "-51", '42sp'],
            "f1": ["25", "abc", "42", "-51", '42sp'],
            "f2": [0, 1, 2, 3, 4],
            "f3": fp3_test,
            "f4": ["Tomato", "Lettuce", "Carrots", "waterMellon"],
        }

        funcs_names = {
            "f0": "ft_first_exception",
            "f1": "ft_raise_exception",
            "f2": "ft_different_errors",
            "f3": "ft_custom_errors",
            "f4": "ft_finally_block",
        }

        ret_expect = {
            "f0": ep0,
            "f1": ep1,
            "f2": ep2,
            "f3": ep3,
            "f4": ep4,
        }

    ret = 0
    i = 0
    clear()
    checker = 0
    print(f"{PINK}RUNNING TESTS FOR PYTHON MODULE 2!{DEFAULT}")
    print(f"{PINK}--------------------------------------------{DEFAULT}", end='')
    tm.sleep(time)
    while ret == 0:
        if i > 4:
            break
        to_get = f"f{i}"
        funcs_to_run = funcs.get(to_get)
        fun_name = funcs_names.get(to_get)
        params = funcs_params.get(to_get)
        expected = ret_expect.get(to_get)
        biggest_name_len = biggest_name(funcs_names)
        if len(fun_name) != biggest_name_len:
            space_times = biggest_name_len - len(fun_name) + 1
        else:
            space_times = 1
        tm.sleep(time)
        if i < 3:
            # print(f"passing test for {fun_name}()...")
            func = funcs_to_run[0]
            tester_func = funcs_to_run[1]
            ret, stats = exec_unit_test(func, tester_func, fun_name, params,
                                        expected, space_times, view, time)
            checker += stats
        elif i == 3:
            # print(f"passing test for {fun_name}()...")            
            class1 = funcs_to_run[0]
            class2 = funcs_to_run[1]
            class3 = funcs_to_run[2]
            tester = funcs_to_run[3]
            ret, stats = exec_unit_class_test0(tester, class1, class2,
                                              class3, fun_name, params,
                                              expected, space_times,
                                              view, time)
            checker += stats
        elif i == 4:
            func = funcs_to_run[0]
            tester = funcs_to_run[1]
            ret, stats = exec_unit_class_test1(tester, func, fun_name,
                                               params, expected, space_times,
                                               view, time)
            checker += stats
        else:
            break
        i += 1
    if ret == 0:
        print(f"\n{PINK}--------------------------------------------{DEFAULT}")
        print(f"{GREEN if checker == 0 else RED}{auto_final_text_s if checker == 0 else auto_final_text_f}{DEFAULT}")
    return ret


def main() -> int:
    parser = argparse.ArgumentParser(description="Tester for Python Module 0 from Ecole 42")
    parser.add_argument("--visual", action="store_true", help="Print functions returns")
    parser.add_argument("--fast", action="store_true", help="run tests faster")

    view = False
    time = 0.5
    args = parser.parse_args()
    if args.visual:
        view = True
    if args.fast:
        time = 0.03
    return exec_tests(view, time)


if __name__ == "__main__":
    main()