# -*- coding:utf-8 -*-
from urllib import parse, request
import http.cookiejar
from bs4 import BeautifulSoup


class USTH:
    def __init__(self):
        # login
        self.loginURL = 'http://60.219.165.24/loginAction.do'
        # grades URL
        '''self.gradesURL = 'http://60.219.165.24/gradeLnAllAction.do?type=ln&oper=qbinfo'''  '''AllSemesterGrade'''
        self.gradesURL = 'http://60.219.165.24/bxqcjcxAction.do?type=ln&oper=qbinfo'    '''ThisSemesterGrade'''
        # cookies and postData
        self.cookies = http.cookiejar.CookieJar()
        zjh = input()
        mm = input()
        self.postData = parse.urlencode({'zjh': zjh, 'mm': mm}).encode('utf8')
        # build opener
        self.opener = request.build_opener(request.HTTPCookieProcessor(self.cookies))
        # result of grade
        self.grade = []

    def getPage(self):
        myRequest = request.Request(url=self.loginURL, data=self.postData)
        self.opener.open(myRequest)
        # get grades
        result = self.opener.open(self.gradesURL)
        html = result.read().decode('gbk')
        bsObj = BeautifulSoup(html, 'html.parser')
        resultList = bsObj.findAll('td', {'align': 'center'})
        for i, each in enumerate(resultList):
            self.grade.append(each.get_text().strip())
            if (i-6) % 7 == 0:
                print(self.grade)
                self.grade = []


if __name__ == '__main__':
    usth = USTH()
    usth.getPage()
