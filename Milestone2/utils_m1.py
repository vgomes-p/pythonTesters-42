# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils_m0.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/19 20:01:16 by vigomes-          #+#    #+#              #
#    Updated: 2026/07/21 18:15:56 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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

list_of_flowers0 = {
    0: {"name": "Rose", "height": 25, "age": 30},
    1: {"name": "Sun Flower", "height": 50, "age": 45},
    2: {"name": "Orchid", "height": 15, "age": 420}
    }

list_of_flowers1 = {
    0: {"name": "Rose", "height": 25.0, "age": 30, "grpd": 0.86, "color": "White"}
}

list_of_plants0 = {
    0: {"name": "Rose", "height": 25, "plant_age": 30},
    1: {"name": "Sunflower", "height": 80, "plant_age": 45},
    2: {"name": "Cactus", "height": 15, "plant_age": 120},
    3: {"name": "Olive", "height": 150, "plant_age": 365},
    4: {"name": "Venus", "height": 9, "plant_age": 1},
    5: {"name": "whatever", "height": 0, "plant_age": 0},
}

list_of_plants1 = {
    0: {"name": "Rose", "height": 25, "plant_age": 30, "grpd": 0.86},
    1: {"name": "Sunflower", "height": 80, "plant_age": 45, "grpd": 0.9},
    2: {"name": "Cactus", "height": 15, "plant_age": 120, "grpd": 0.15},
    3: {"name": "Olive", "height": 150, "plant_age": 365, "grpd": 0.02},
    4: {"name": "Venus", "height": 9, "plant_age": 1, "grpd": 0.5},
    5: {"name": "whatever", "height": 0, "plant_age": 1, "grpd": 2.0},
}

list_of_plants2 = {
    0: {"name": "Rose", "height": 25, "plant_age": 30, "grpd": 0.86},
    1: {"name": "Sunflower", "height": 80, "plant_age": 45, "grpd": 0.9},
    2: {"name": "Cactus", "height": -15, "plant_age": 120, "grpd": 0.15},
    3: {"name": "Olive", "height": 150, "plant_age": -365, "grpd": 0.02},
    4: {"name": "Venus", "height": 9, "plant_age": 1, "grpd": 0.5},
    5: {"name": "whatever", "height": 0, "plant_age": 1, "grpd": 2.0},
}

list_of_trees = {
    0: {"name": "Oak", "height": 200.0, "age": 1095, "grpd": 10.0, "trunk_diameter": 5.0}
}

list_of_vegetables = {
    0: {"name": "Tomato", "height": 5.0, "age": 10, "grpd": 2.1, "season": "April", "nutri": 1}
}

TEXTS = {
    "f0": {"init_text": "=== Welcome to My Garden ===\n", "mid_text": None, "end_text": "=== End of Program ===\n"},
    "f1": {"init_text": "=== Garden Plant Registry ===\n", "mid_text": None, "end_text": None},
    "f2": {"init_text": "=== Day 1 ===\n", "mid_text": "=== Day 7 ===\n", "end_text": None},
    "f3": {"init_text": None, "mid_text": None, "end_text": None},
    "f4": {"init_text": "", "mid_text": "", "end_text": ""},
    "f5": {"init_text": "", "mid_text": "", "end_text": ""},
    "f6": {"init_text": "", "mid_text": "", "end_text": ""},
    "f7": {"init_text": "", "mid_text": "", "end_text": ""},
}

MID_IDS = {
    0: -1,
    1: -1,
    2: 2,
    3: -1,
    # 4: 4,
    # 5: 5,
    # 6: 6,
}

END_IDS = {
    0: 1,
    1: -1,
    2: -1,
    3: -1,
    # 4: 4,
    # 5: 5,
    # 6: 6,
}

f0e = {
    0: "=== Welcome to My Garden ===\nPlant: Rose\nHeight: 25cm\nAge: 30 days\n=== End of Program ===\n",
    1: "=== Welcome to My Garden ===\nPlant: Sun Flower\nHeight: 50cm\nAge: 45 days\n=== End of Program ===\n",
    2: "=== Welcome to My Garden ===\nPlant: Orchid\nHeight: 15cm\nAge: 420 days\n=== End of Program ===\n",
    }

f1e = {
    0: "=== Garden Plant Registry ===\nRose: 25.0cm, 30 days old\n",
    1: "=== Garden Plant Registry ===\nSunflower: 80.0cm, 45 days old\n",
    2: "=== Garden Plant Registry ===\nCactus: 15.0cm, 120 days old\n",
    3: "=== Garden Plant Registry ===\nOlive: 150.0cm, 365 days old\n",
    4: "=== Garden Plant Registry ===\nVenus: 9.0cm, 1 days old\n",
    5: "=== Garden Plant Registry ===\nwhatever: 0.0cm, 0 days old\n"
    }

f2e = {
    0: "=== Day 1 ===\nRose: 25.0cm, 30 days old\n=== Day 7 ===\nRose: 31.0cm, 37 days old\nGrowth this week: +6.02cm\n",
    1: "=== Day 1 ===\nSunflower: 80.0cm, 45 days old\n=== Day 7 ===\nSunflower: 86.3cm, 52 days old\nGrowth this week: +6.30cm\n",
    2: "=== Day 1 ===\nCactus: 15.0cm, 120 days old\n=== Day 7 ===\nCactus: 16.1cm, 127 days old\nGrowth this week: +1.05cm\n",
    3: "=== Day 1 ===\nOlive: 150.0cm, 365 days old\n=== Day 7 ===\nOlive: 150.1cm, 372 days old\nGrowth this week: +0.14cm\n",
    4: "=== Day 1 ===\nVenus: 9.0cm, 1 days old\n=== Day 7 ===\nVenus: 12.5cm, 8 days old\nGrowth this week: +3.50cm\n",
    5: "=== Day 1 ===\nwhatever: 0.0cm, 1 days old\n=== Day 7 ===\nwhatever: 14.0cm, 8 days old\nGrowth this week: +14.00cm\n"
    }

f3e1 = {
    0: "Created: Rose: 25.0cm, 30 days old\nTotal of plants: 1\n",
    1: "Created: Sunflower: 80.0cm, 45 days old\nTotal of plants: 2\n",
    2: "Created: Cactus: 15.0cm, 120 days old\nTotal of plants: 3\n",
    3: "Created: Olive: 150.0cm, 365 days old\nTotal of plants: 4\n",
    4: "Created: Venus: 9.0cm, 1 days old\nTotal of plants: 5\n",
    5: "Created: whatever: 0.0cm, 1 days old\nTotal of plants: 6\n",
}

f3e2 = {
    0: "Created: Rose: 25.0cm, 30 days old\nno class variable like total_plant\n",
    1: "Created: Sunflower: 80.0cm, 45 days old\nno class variable like total_plant\n",
    2: "Created: Cactus: 15.0cm, 120 days old\nno class variable like total_plant\n",
    3: "Created: Olive: 150.0cm, 365 days old\nno class variable like total_plant\n",
    4: "Created: Venus: 9.0cm, 1 days old\nno class variable like total_plant\n",
    5: "Created: whatever: 0.0cm, 1 days old\nno class variable like total_plant\n",
}

f3e3 = [
    "Created: Rose: 25.0cm, 30 days old\nCreated: Sunflower: 80.0cm, 45 days old\nCreated: Cactus: 15.0cm, 120 days old\nCreated: Olive: 150.0cm, 365 days old\nCreated: Venus: 9.0cm, 1 days old\nCreated: whatever: 0.0cm, 1 days old\nTotal of plants: 6\n",
    "Created: Rose: 25.0cm, 30 days old\nCreated: Sunflower: 80.0cm, 45 days old\nCreated: Cactus: 15.0cm, 120 days old\nCreated: Olive: 150.0cm, 365 days old\nCreated: Venus: 9.0cm, 1 days old\nCreated: whatever: 0.0cm, 1 days old\nno class variable like total_plant\n"
    ]


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
