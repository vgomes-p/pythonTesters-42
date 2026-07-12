# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    module0.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/12 14:55:15 by vigomes-          #+#    #+#              #
#    Updated: 2026/07/12 15:19:25 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout
import time as tm
import os
import subprocess
import argparse


DEFAULT = "\033[m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YLOW = "\033[1;33m"
PINK = "\033[1;35m"
CYAN = "\033[1;36m"
INVERT = "\033[1;4;7;97m"
BOLD = "\033[1m"

auto_final_text_s = "CONGRATS, ALL RAN SUCESSFULLY!"
auto_final_text_f = "SOMETHING IS WRONG, REVIEW YOUR CODE!"
ex1expect0 = """Garden: Community Garden
Status: Growing well!
"""
ex1expect1 = """Garden: 42 Sao Paulo
Status: Growing well!
"""
ex6expect0 = """Day 0
Day 1
Day 2
Day 3
Day 4
Day 5
Harvest time!
"""
ex6expect1 = """Day 0
Day 1
Day 2
Day 3
Day 4
Day 5
Day 6
Day 7
Day 8
Day 9
Day 10
Harvest time!
"""
ex6expect2 = """Day 0
Day 1
Day 2
Day 3
Day 4
Day 5
Day 6
Day 7
Day 8
Day 9
Day 10
Day 11
Day 12
Day 13
Day 14
Day 15
Day 16
Day 17
Day 18
Day 19
Day 20
Day 21
Day 22
Day 23
Day 24
Day 25
Day 26
Day 27
Day 28
Day 29
Day 30
Day 31
Day 32
Day 33
Day 34
Day 35
Day 36
Day 37
Day 38
Day 39
Day 40
Day 41
Day 42
Harvest time!
"""


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


def exec_no_input(function, function_name: str, expect: str, space_time: int = 1, view: bool=False, time: float=0.5) -> tuple[int, int]:
    stats = 0
    print(f"{CYAN}\n{function_name}:{' ' * space_time}{DEFAULT}", end=('\n' if view else ''), flush=True)
    tm.sleep(time)
    try:
        buffer = StringIO()
        with redirect_stdout(buffer):
            function()
        output = buffer.getvalue()
        if output == expect:
            print('✅', end='', flush=True)
        else:
            print('❌', end='', flush=True)
            stats += 1
        if view:
            print(f"\nEXPECTED:\n{expect}\nOUTPUT:\n{output}")
    except AttributeError as e:
        error_message(f"Could not find function {function_name}() in file")
        error_message(e, False)
        return 1, 1
    except Exception as e:
        error_message(f"Error running function {function_name}(): {e}")
        error_message(f"Check the code for systax errors!", False)
        return 1, 1
    printnl()
    return 0, stats


def exec_inputs(function, function_name: str, inputs: dict, expected: dict, space_time: int = 1, view: bool=False, time: float=0.5) -> tuple[int, int]:
    stats = 0
    print(f"{CYAN}\n{function_name}:{' ' * space_time}{DEFAULT}", end=('\n' if view else ''), flush=True)
    for key in inputs:
        tm.sleep(time)
        try:
            buffer = StringIO()
            with patch("builtins.input", side_effect=inputs[key]):
                with redirect_stdout(buffer):
                    function()
            output = buffer.getvalue()
            if output == expected[key]:
                print('✅', end='', flush=True)
            else:
                print('❌', end='', flush=True)
                stats = 1
            if view:
                print(f"\nEXPECTED:\n{expected[key]}\n\nOUTPUT:\n{output}")
        except Exception as e:
            error_message(f"Serious error on running {function_name}(): {e}")
            return 1, 1
    printnl()
    return 0, stats


def exec_params(function, function_name: str, parameters: dict, expected: dict, space_time: int = 1, view: bool=False, time: float=0.5) -> tuple[int, int]:
    i = 0
    stats = 0
    print(f"{CYAN}\n{function_name}:{' ' * space_time}{DEFAULT}", end=('\n' if view else ''), flush=True)
    for parameter in parameters.values():
        tm.sleep(time)
        expect = expected[i]
        seed = parameter["seed"]
        quant = parameter["quant"]
        unit = parameter["unit"]
        buffer = StringIO()
        try:
            with redirect_stdout(buffer):
                function(seed, quant, unit)
            output = buffer.getvalue()
            if output == expect:
                print('✅', end='', flush=True)
            else:
                print('❌', end='', flush=True)
                stats = 1
            if view:
                print(f"\nEXPECTED:\n{expect}\nOUTPUT:\n{output}")
        except Exception as e:
            error_message(f"Serious error on running {function_name}(): {e}")
            return 1, 1
        i += 1;
    printnl()
    return 0, stats


def biggest_name(dict_names: dict) -> int:
    biggest = 0
    for code in dict_names:
        name_len = len(dict_names[code])
        if name_len >= biggest:
            biggest = name_len
    return biggest


def exec_tests(view: bool, time: float) -> int:
    try:
        from ex0.ft_hello_garden import ft_hello_garden
        from ex1.ft_garden_name import ft_garden_name
        from ex2.ft_plot_area import ft_plot_area
        from ex3.ft_harvest_total import ft_harvest_total
        from ex4.ft_plant_age import ft_plant_age
        from ex5.ft_water_reminder import ft_water_reminder
        from ex6.ft_count_harvest_iterative import ft_count_harvest_iterative
        from ex6.ft_count_harvest_recursive import ft_count_harvest_recursive
        from ex7.ft_seed_inventory import ft_seed_inventory
    except ImportError as e:
        error_message(e)
    finally:
        funcs = {
            "f0": ft_hello_garden,
            "f1": ft_garden_name,
            "f2": ft_plot_area,
            "f3": ft_harvest_total,
            "f4": ft_plant_age,
            "f5": ft_water_reminder,
            "f6": ft_count_harvest_iterative,
            "f7": ft_count_harvest_recursive,
            "f8": ft_seed_inventory,
        }

        funcs_names = {
            "f0": "ft_hello_garden",
            "f1": "ft_garden_name",
            "f2": "ft_plot_area",
            "f3": "ft_harvest_total",
            "f4": "ft_plant_age",
            "f5": "ft_water_reminder",
            "f6": "ft_count_harvest_iterative",
            "f7": "ft_count_harvest_recursive",
            "f8": "ft_seed_inventory",
        }

        funcs_inputs = {
            "f1": {0: ["Community Garden"], 1: ["42 Sao Paulo"]},
            "f2": {0: [5, 3], 1: [6, 7], 2: [10, 4]},
            "f3": {0: [5, 8, 3], 1: [10, 13, 19]},
            "f4": {0: [75], 1: [42], 3: [9999999999]},
            "f5": {0: [2], 1: [4], 2: [42]},
            "f6": {0: [5], 1: [10], 2: [42]},
            "f7": {0: [5], 1: [10], 2: [42]},
        }

        funcs_inputs_expect = {
            "f1": {0: ex1expect0, 1: ex1expect1},
            "f2": {0: "Plot area: 15\n", 1: "Plot area: 42\n", 2: "Plot area: 40\n"},
            "f3": {0: "Total harvest: 16\n", 1: "Total harvest: 42\n"},
            "f4": {0: "Plant is ready to harvest!\n", 1: "Plant needs more time to grow.\n", 3: "Plant is ready to harvest!\n"},
            "f5": {0: "Plant is fine.\n", 1: "Water the plant!\n", 2: "Water the plant!\n"},
            "f6": {0: ex6expect0, 1: ex6expect1, 2: ex6expect2},
            "f7": {0: ex6expect0, 1: ex6expect1, 2: ex6expect2},
        }

        params = {
            0: {"seed": "tomato         ", "quant": 15, "unit": "packets"},
            1: {"seed": "      caRroT", "quant": 8, "unit": "grams"},
            2: {"seed": "lettUcE", "quant": 12, "unit": "area"},
            3: {"seed": "     APPLES   ", "quant": 42, "unit": "packets"},
            4: {"seed": "mangO", "quant": 4, "unit": "not valid"},
        }

        params_expect = {
            0: "Tomato seeds: 15 packets available\n",
            1: "Carrot seeds: 8 grams total\n",
            2: "Lettuce seeds: cover 12 square meter\n",
            3: "Apples seeds: 42 packets available\n",
            4: "Unknown unit type\n",
        }

    ret = 0
    i = 0;
    clear()
    checker = 0
    print(f"{PINK}RUNNING TESTS FOR PYTHON MODULE 0!{DEFAULT}")
    print(f"{PINK}-----------------------------------------{DEFAULT}", end='')
    tm.sleep(time)
    while ret == 0:
        if i > 8:
            break
        to_get = f"f{i}"
        to_run = funcs.get(to_get)
        fun_name = funcs_names.get(to_get)
        ips = funcs_inputs.get(to_get)
        ips_expec = funcs_inputs_expect.get(to_get)
        biggest_name_len = biggest_name(funcs_names)
        if len(fun_name) != biggest_name_len:
            space_times = biggest_name_len - len(fun_name) + 1
        else:
            space_times = 1
        tm.sleep(time)
        if i == 0:
            ret, stats = exec_no_input(to_run, fun_name, "Hello, Garden Community!\n", space_times, view, time)
            checker += stats
        elif i == 8:
            ret, stats = exec_params(to_run, fun_name, params, params_expect, space_times, view, time)
            checker += stats
        else:
            ret, stats = exec_inputs(to_run, fun_name, ips, ips_expec, space_times, view, time)
            checker += stats
        i += 1
    if ret == 0:
        print(f"\n{PINK}-----------------------------------------{DEFAULT}")
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
    elif args.fast:
        time = 0.05
    return exec_tests(view, time)


if __name__ == "__main__":
    main()
