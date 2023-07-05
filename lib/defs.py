import json
import webbrowser

import pygame
import requests


def var_check(version):
    latest_response = requests.get(
        "https://api.github.com/repos/newkincode/simple_farming_game/releases/latest"
    )
    latest_releases = json.loads(latest_response.text)
    latest_tag: str = latest_releases["tag_name"]
    latest_var = [list(latest_tag.split("_"))[0], latest_tag.split("_")[1].split(".")]
    var_ranking = {"alpha": 0, "beta": 1, "release": 2}
    if latest_var[0] == [0]:
        latest_ver_num = list(map(int, latest_var[1]))
        current_ver_num = [int(x) for x in version[1:]]
        if latest_ver_num > current_ver_num:
            print("최신 버전이 있습니다. 릴리즈 페이지에서 업데이트 해주세요.")
            webbrowser.open("https://github.com/newkincode/simple_farming_game")
        else:
            print("최신 버전을 사용 중입니다.")
        del latest_ver_num
        del current_ver_num
    else:
        if var_ranking[latest_var[0]] > var_ranking[version[0]]:
            print("최신 버전이 있습니다. 릴리즈 페이지에서 업데이트 해주세요.")
            webbrowser.open("https://github.com/newkincode/simple_farming_game")
        else:
            print("최신 버전을 사용 중입니다.")

    del latest_response
    del latest_releases
    del latest_tag
    del latest_var
    del var_ranking


def get_image_height(image: pygame.Surface) -> int:
    return image.get_height()


def get_image_width(image: pygame.Surface):
    try:
        return image.get_width()
    except pygame.error:
        print("이미지를 열 수 없거나 잘못된 형식입니다.")
        return None
