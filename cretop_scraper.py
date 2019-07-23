#-*- coding:utf-8 -*-

from selenium import webdriver
import configparser
import os


def config_init():
    cur_path = os.path.abspath(os.path.dirname(__file__))
    conf_path = os.path.join(cur_path, "config\info.conf")
    config = configparser.ConfigParser()
    config.read(conf_path, 'utf-8')
    return config


def load_driver(config):
    driver = webdriver.Ie(config['WEBDRIVER']['webdriver_path'])
    driver.implicitly_wait(3)
    return driver


def page_connect(driver, config):
    driver.get(config['CRETOP']['cretop_url'])


def main():
    config = config_init()
    driver = load_driver(config)
    page_connect(driver, config)

    ## Login Session
    driver.find_element_by_id('in_id').send_keys(config['CRETOP']['cretop_id'])
    driver.find_element_by_id('in_pw').send_keys(config['CRETOP']['cretop_pw'])

    driver.find_element_by_id('loginBtn1').click()

    ## personal authentification - 필요없을 수 있음
    # driver.find_element_by_name('indvInfoColAgrYn').click()
    # driver.find_element_by_name('prpIdInfoAgrYn').click()
    #
    # driver.find_element_by_name('name').send_keys(config['CRETOP']['cretop_name'])
    # driver.find_element_by_name('pid1').send_keys(config['CRETOP']['cretop_pid1'])
    # driver.find_element_by_name('pid2').send_keys(config['CRETOP']['cretop_pid2'])
    #
    # driver.find_element_by_id('CMMBR02R1').click()

    ## 문자 인증 - 일단 skip

    ## 로그인 세션 연장


    html = driver.page_source
    print(html)

    sleep(100)
    driver.find_element_by_class_name('loginPxad').click()
    ## 정보를 가져올 회사 리스트 조회
    ## 고민 대상 - 검색할 대상 회사의 범위를 어떤 기준으로 가져올 것인지....
    ## 고민 대상 - 검색 도중 세션이 끊길 수 있음. 재 연결하고 긁어오던 부분부터 가져올 방법 고민

    ## 페이지 순회

    ## 엑셀로 파일 저장

if __name__ == '__main__':
    main()