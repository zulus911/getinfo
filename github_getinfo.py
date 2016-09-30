#!/usr/bin/env python

from github import Github
from argparse import ArgumentParser



class GetInfo:
    UserName = ''
    Password = ''
    Token = ''
    def __init__(self, user='', password='', token=''):
        self.UserName = user
        self.Password = password
        self.Token = token

    def diff_auth(self):
        if self.Token != '':
            try:
                return Github(self.Token)
            except:
                print "bad token"
                exit(2)
        else:
            try:
                return Github(self.UserName, self.Password)
            except:
                print "Bad login or password"
                exit(2)

    def get_username(self):
        g = self.diff_auth()
        return g.get_user('github').get_repo('hubot').get_releases()



if __name__ == "__main__":
    
    parser_cli = ArgumentParser()
    parser_cli.add_argument("--user", action="store", dest="user")
    parser_cli.add_argument("--pass", action="store", dest="passw")
    parser_cli.add_argument("--token", action="store", dest="token")
    cli_parsed = parser_cli.parse_args()
    if cli_parsed.token != None:
        rip = GetInfo(token=cli_parsed.token)
        for i in rip.get_username():
            print str(i)
    elif cli_parsed.user != None and cli_parsed.passw != None:
        rip = GetInfo(user = cli_parsed.user, password = cli_parsed.passw)
        try:
            f = open("/dev/shm/github_getinfo.cache", "w+")
            f.write(cli_parsed.user)
            f.close()
        except:
            print ("Can not write to cache file. Only pass input not worked")
        for i in rip.get_username():
            print str(i)
    elif cli_parsed.passw != None and cli_parsed.user == None:
        try:
            f = open("/dev/shm/github_getinfo.cache", "r")
        except:
            print "No previous success login. Please use option --user for setup your login"
            exit(4)
        user = f.read()
        f.close
        rip = GetInfo(user = user, password = cli_parsed.passw)
        for i in rip.get_username():
            print str(i.tag_name)
            print str(i.url)
            print str(i.author._rawData['login'])
            print str(i.title)
            print str(i.body)

    else:
        print "Please use --hepl for seing how use this script"
        exit(1)

