#!/usr/bin/env python

#from github import Github
from github import GitHub
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
                print "2"
                #return Github(self.Token)
                return GitHub(access_token=self.Token)
            except:
                print "bad token"
                exit(2)
        else:
            try:
                #return Github(self.UserName, self.Password)
                return GitHub(username=self.UserName, password=self.Password)
            except:
                print "Bad login or password"
                exit(2)

    def get_username(self):
        g = self.diff_auth()
        print "3"
        #return g.get_user('zulus911').get_()repo('getinfo').get_releases()
        return g.repos('github')('hubot').releases().get()



if __name__ == "__main__":
    
    parser_cli = ArgumentParser()
    parser_cli.add_argument("--user", action="store", dest="user")
    parser_cli.add_argument("--pass", action="store", dest="passw")
    parser_cli.add_argument("--token", action="store", dest="token")
    cli_parsed = parser_cli.parse_args()
    if cli_parsed.token != None:
        print "1"
        rip = GetInfo(token=cli_parsed.token)
        
        for i in rip.get_username():
            print i.body
            print i.author.login
            print i.tag_name
            print i.html_url
    elif cli_parsed.user != None and cli_parsed.passw != None:
        rip = GetInfo(user = cli_parsed.user, password = cli_parsed.passw)
        try:
            f = open("/dev/shm/github_getinfo.cache", "w+")
            f.write(cli_parsed.user)
            f.close()
        except:
            print ("Can not write to cache file. Only pass input not worked")
        for i in rip.get_username():
            print i.body
            print i.author.login
            print i.tag_name
            print i.html_url
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
            print i.body
            print i.author.login
            print i.tag_name
            print i.html_url
    else:
        print "Please use --hepl for seing how use this script"
        exit(1)

