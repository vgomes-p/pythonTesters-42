# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    module1.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/12 14:55:15 by vigomes-          #+#    #+#              #
#    Updated: 2026/07/20 20:52:01 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# YOU MIGHT WANT TO READ THIS
"""
First of all, i'm also asking me what the fuck is this script.

Second of all, it all started beautifully, but after ex1 I notice that people
will implement the assignments differently and it was in that moment that i knew
I fucked up. That's how what should be simple became a monster (because I refuse
to ask AI to do everything, I want to learn by making the worst code I can and
do it better the next time.)

I don't recomend you to modify this code at any line, it might break and you
probably will want to fix it and spend a long time on it. You better go learn
something new.

As a warn, this is the amount of days spend on this code (fixing, improving or
implementing something): 3 days
"""

from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout
import time as tm
import argparse
from utils_m0 import list_of_flowers0, list_of_flowers1, list_of_plants0, list_of_plants1, list_of_plants2, list_of_trees, list_of_vegetables
from utils_m0 import clear, printnl, error_message, biggest_name
from utils_m0 import DEFAULT, RED, GREEN,  PINK, CYAN
from utils_m0 import TEXTS, MID_IDS, END_IDS
from utils_m0 import f0e, f1e, f2e, f3e1, f3e2, f3e3
import pdb


auto_final_text_s = "CONGRATS, ALL RAN SUCESSFULLY!"
auto_final_text_f = "SOMETHING IS WRONG, REVIEW YOUR CODE!"


def build_args(parameter: list) -> list:
    args = [
        parameter["name"],
        parameter["height"]
    ]
    if "plant_age" in parameter:
        args.append(parameter["plant_age"])
    if "grpd" in parameter:
        args.append(parameter["grpd"])
    return args


def exec_no_class(function, function_name: str, parameters: dict, in_params: list, expected: dict, texts: dict, space_time: int = 1, view: bool=False, time: float=0.5) -> tuple[int, int]:
    i = 0
    stats = 0
    init_text = texts.get("init_text")
    end_text = texts.get("end_text")
    print(f"{CYAN}\n{function_name}:{' ' * space_time}{DEFAULT}", end=('\n' if view else ''), flush=True)
    for parameter in parameters.values():
        tm.sleep(time)
        expect = expected[i]
        param1 = parameter[str(in_params[0])]
        param2 = int(parameter[str(in_params[1])])
        param3 = int(parameter[str(in_params[2])])
        buffer = StringIO()
        try:
            with redirect_stdout(buffer):
                print(init_text if init_text else "", end = '')
                function(param1, param2, param3)
                print(end_text if end_text else "", end = '')
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


def exec_mod(fclass, id: int, modules: dict, texts: dict, args: list, assign_name: str) -> str:
    # pdb.set_trace()
    init_text = texts.get("init_text")
    mid_text = texts.get("mid_text")
    end_text = texts.get("end_text")
    temp = 0
    
    buffer = StringIO()
    i = 0
    with redirect_stdout(buffer):
        try:
            obj = fclass(*args)
            for module in modules:
                # print(f"DEBUG: module: {module} | id: {id} | i: {i} | MID_IDS: {MID_IDS[id]} | END_IDS: {END_IDS[id]}")
                if i == 0:
                    print(init_text if init_text else "", end='')
                if i == MID_IDS[id]:
                    print(mid_text if mid_text else "", end='')
                if i == END_IDS[id]:
                    print(end_text if end_text else "", end='')
                if id == 2 and i == 1:
                    temp = getattr(obj, module)(7)
                else:
                    getattr(obj, module)()
                    if id == 2 and i == 2:
                        print(f"Growth this week: +{temp:.2f}cm")
                i += 1
        except Exception as e:
            error_message(f"Serious error on running {assign_name}: {e}")
            return None
    return buffer.getvalue()


def exec_special3(fclass, id: int, modules: dict, assign_name: str, parameters: dict, expected: dict, view: bool=False, time: float=0.5) -> int:
    expected1 = expected.get(1)
    expected2 = expected.get(2)
    expected3 = expected.get(3)
    stats = 0
    i = 0

    for p in parameters:
        plant = parameters[p]
        buffer1 = StringIO()
        with redirect_stdout(buffer1):
            try:
                plants = fclass(plant["name"], plant["height"], plant["age"], plant["grpd"])
                try:
                    print(f"Total of plants: {plants.total_plants}")
                except:
                    print("no class variable like total_plant")
            except Exception as e:
                error_message(f"Serious error on running {assign_name}: {e}")
                return -1
        output = buffer1.getvalue()
        if output == expected1:
            print('✅', end='', flush=True)
        elif output == expected2:
            print('✅', end='', flush=True)
        else:
            print('❌', end='', flush=True)
            stats += 1
        if view:
            print(f"\nEXPECTED 1:\n{expected1[i]}\nEXPECTED 2:\n{expected2[i]}\nOUTPUT:\n{output}")
        i += 1

    i = 0
    buffer2 = StringIO()
    with redirect_stdout(buffer2):
        try:
            for p in parameters:
                plant = parameters[p]
                plants = fclass(plant["name"], plant["height"], plant["age"], plant["grpd"])
            try:
                print(f"Total of plants: {plants.total_plants}")
            except:
                print("no class variable like total_plant")
        except Exception as e:
                error_message(f"Serious error on running {assign_name}: {e}")
                return -1
    output = buffer1.getvalue()
    if output == expected3[0]:
        print('✅', end='', flush=True)
    elif output == expected3[1]:
        print('✅', end='', flush=True)
    else:
        print('❌', end='', flush=True)
        stats += 1
    if view:
        print(f"\nFINAL EXPECTED 1:\n{expected1[i]}\nFINAL EXPECTED 2:\n{expected2[i]}\nOUTPUT:\n{output}")
        i += 1
    return stats


def exec_class(fclass, id: int, modules: dict, assign_name: str, parameters: dict, expected: dict, texts: dict, space_time: int = 1, view: bool=False, time: float=0.5) -> tuple[int, int]:
    i = 0
    stats = 0
    print(f"{CYAN}\n{assign_name}:{' ' * space_time}{DEFAULT}", end=('\n' if view else ''), flush=True)
    if i == 3:
        ret = exec_special3(fclass, id, modules, assign_name, parameters, expected, view, time)
        if ret == -1:
            return 1, 1
        else:
            return 0, stats
    else:
        for i, parameter in parameters.items():
            tm.sleep(time)
            try:
                args = build_args(parameter)
                output = exec_mod(fclass, id, modules, texts, args, assign_name)
                if output == expected[i]:
                    print('✅', end='', flush=True)
                else:
                    print('❌', end='', flush=True)
                    stats = 1
                if view:
                    print(f"\nEXPECTED:\n{expected[i]}\nOUTPUT:\n{output}")
            except Exception as e:
                error_message(f"Serious error on running {assign_name}: {e}")
                return 1, 1
            i += 1;
    printnl()
    return 0, stats


def exec_tests(view: bool, time: float) -> int:
    try:
        from ex0.ft_garden_intro import ft_my_garden
        from ex1.ft_garden_data import Plant as Pl1
        from ex2.ft_plant_growth import Plant as Pl2
        from ex3.ft_plant_factory import Plant as Pl3
        from ex4.ft_garden_security import Plant as Pl4
        from ex5.ft_plant_types import Flower
        from ex5.ft_plant_types import Tree
        from ex5.ft_plant_types import Vegetables
        up_coming = "up_coming"
    except ImportError as e:
        error_message(e)
    finally:
        funcs = {
            "f0": ft_my_garden,
            "f1": Pl1,
            "f2": Pl2,
            "f3": Pl3,
            "f4": Pl4,
            "f5": Flower,
            "f6": Tree,
            "f7": Vegetables,
            "f8": up_coming,
        }

        funcs_names = {
            "f0": "ft_my_garden()",
            "f1": "Gerden Data",
            "f2": "Plant Growth",
            "f3": "Plant Factory",
            "f4": "Garden Security",
            # "f5": "Plant Type: Flower",
            # "f6": "Plant Type: Tree",
            # "f7": "Plant Type: Vegetables",
            # "f8": "ft_seed_inventory",
        }

        funcs_params = {
            "f0": list_of_flowers0,
            "f1": list_of_plants0,
            "f2": list_of_plants1,
            "f3": list_of_plants1,
            # "f4": list_of_plants2,
            # "f5": list_of_flowers1,
            # "f6": list_of_trees,
            # "f7": list_of_vegetables,
        }

        in_params0 = ["name", "height", "age"]

        class_modules = {
            "f0": ["show"],
            "f1": ["show"],
            "f2": ["show", "grow", "show"],
            "f3": [None],
            # "f4": ["show", "grow"],
            # "f5": ["show", "grow"],
            # "f6": ["show", "grow"],
            # "f7": ["show", "grow"],
        }

        ret_expect = {
            "f0": f0e,
            "f1": f1e,
            "f2": f2e,
            "f3": {1: f3e1, 2: f3e2, 3: f3e3},
            # "f4": {0: [], 1: [], 2: [], 3: [], 4: [], 5: []},
            # "f5": {0: [], 1: [], 2: [], 3: [], 4: [], 5: []},
            # "f6": {0: [], 1: [], 2: [], 3: [], 4: [], 5: []},
            # "f7": {0: [], 1: [], 2: [], 3: [], 4: [], 5: []},
        }

    ret = 0
    i = 0;
    clear()
    checker = 0
    print(f"{PINK}RUNNING TESTS FOR PYTHON MODULE 1!{DEFAULT}")
    print(f"{PINK}-----------------------------------------{DEFAULT}", end='')
    tm.sleep(time)
    while ret == 0:
        if i > 8:
            break
        to_get = f"f{i}"
        to_run = funcs.get(to_get)
        fun_name = funcs_names.get(to_get)
        params = funcs_params.get(to_get)
        params_expect = ret_expect.get(to_get)
        modules = class_modules.get(to_get)
        texts = TEXTS.get(to_get)
        biggest_name_len = biggest_name(funcs_names)
        if i == 0:
            in_params = in_params0
        if len(fun_name) != biggest_name_len:
            space_times = biggest_name_len - len(fun_name) + 1
        else:
            space_times = 1
        tm.sleep(time)
        if i == 0:
            ret, stats = exec_no_class(to_run, fun_name, params, in_params, params_expect, texts, space_times, view, time)
            checker += stats
        elif i == 8:
            pass
            # ret, stats = exec_params(to_run, fun_name, params, params_expect, space_times, view, time)
            # checker += stats
        else:
            ret, stats = exec_class(to_run, i, modules, fun_name, params, params_expect, texts, space_times, view, time)
            checker += stats
            if i == 3:
                break
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
