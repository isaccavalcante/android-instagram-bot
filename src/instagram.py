#-*- coding: utf-8 -*-
from uiautomator import device as d
from bs4 import BeautifulSoup
import time
import asyncio
import os

if not os.path.exists("skip.txt"):
    open("skip.txt", "a").close()

def type_word(word):
    for char in word:
        key_code = ord(char) - 68
        d.press(key_code)

def dump():
    xml = d.dump("screen.xml")
    with open("screen.csv", 'w', encoding="utf-8") as f:
        f.write("text,content-desc,id" + "\n")
        soup = BeautifulSoup(xml, "html.parser")
        for node in soup.find_all("node"):
            line = f"{node['text']},{node['content-desc']},{node['resource-id']}"
            f.write(line + "\n")

def enter_instagram():
    print("[+] Openning instagram")
    d.press.home()
    d(text="Instagram").click()

def follow_commentators():
    enter_instagram()
    d(description="Search and Explore").click()
    d(text="Search").click()
    d(text="Search").click()
    username = "filipedeschamps"
    type_word(username)
    d(text=username).click()
    d(descriptionContains="at Row 1, Column 1").click()
    d(textContains="View all").click()
    d(resourceId="com.instagram.android:id/row_comment_imageview").click()
    d(text="Follow").click()
    d.press.back()
    # WIP


def pretend_normal_usage():
    #dump()
    d(description="Home", className="android.widget.FrameLayout").click()
    #d.press.back()
    d(descriptionContains="'s story at column")[1].drag.to(descriptionContains="'s story at column")
    d.press.back()
    d(descriptionContains="'s story at column")[1].click()
    time.sleep(3)
    d.press.back()
    #d(description="Image").swipe.up(steps=10)
    #time.sleep(5)
    d(description="Profile").click()
    d(description="Profile").click()
    #d(text="Following").click()

def unfollow_all():
    enter_instagram()
    d(description="Profile").click()
    d(description="Profile").click()
    d(text="Following").click()
    count = 0
    while True:
        d(text="Following").click()
        if d(text="Unfollow").exists:
            d(text="Unfollow").click()
        print(f"[+] Unfollowed {count + 1} accounts")
        count += 1
        d(text="Follow")[-1].drag.to(textContains="Followers")
        pretend_normal_usage()
        #time.sleep(30)

def add_to_skip_list(username):
    with open("skip.txt", 'a+', encoding="utf-8") as f:
        f.write(username + "\n")

def get_to_skip_list():
    to_skip = []
    with open("skip.txt", 'r', encoding="utf-8") as f:
        for line in f.readlines():
            to_skip.append(line.strip())
    return to_skip

def unfollow_unfollowers():
    to_skip = get_to_skip_list()
    d(description="Profile").click()
    d(description="Profile").click()
    my_username = d(resourceId="com.instagram.android:id/title_view").info["text"]
    print(f"[+] Logged in as {my_username}")
    d(text="Following").click()
    
    
    unfollowed = False
    while not unfollowed:
        following_username = d(resourceId="com.instagram.android:id/follow_list_username").info["text"]
        #following_username_name = d(resourceId="com.instagram.android:id/follow_list_subtitle").info["text"]
        print(following_username)
        if following_username in to_skip:
            print(f"[+] Skipping {following_username}")
            #d(description=f"Following {following_username_name} button").drag.to(resourceId="com.instagram.android:id/action_bar_root")
            d(text=f"Following").drag.to(textContains="Followers")
        else:
            unfollowed = True

    d(text=following_username).click()
    d(text="Following").click()
    if d(text=my_username).exists: # user follows me
        d.press.back()
        d.press.back()
        add_to_skip_list(following_username)
    else: # user does not follow me
        d.press.back()
        d.press.back()
        print(f"[+] Unfollowing {following_username}")
        d(text=f"Following").click()
        if d(text="Unfollow").exists:
            d(text="Unfollow").click()
    #d(text=f"Following").drag.to(textContains="Followers")
    pretend_normal_usage()    


enter_instagram()

try:
    while True:
        unfollow_unfollowers()
except Exception as e:
    print("[-] An error ocurrend. Dumping screen.csv")
    dump()