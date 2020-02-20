from uiautomator import device as d
from bs4 import BeautifulSoup
import time
import asyncio


def type_word(word):
    for char in word:
        key_code = ord(char) - 68
        d.press(key_code)

def dump():
    xml = d.dump("screen.xml")
    with open("screen.csv", 'w') as f:
        f.write("text,content-desc,id" + "\n")
        soup = BeautifulSoup(xml, "html.parser")
        for node in soup.find_all("node"):
            line = f"{node['text']},{node['content-desc']},{node['resource-id']}"
            f.write(line + "\n")
            

def enter_instagram():
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
    dump()
    d(description="Home", className="android.widget.FrameLayout").click()
    #d.press.back()
    d(descriptionContains="'s story at column")[1].drag.to(descriptionContains="'s story at column")
    d.press.back()
    d(descriptionContains="'s story at column")[1].click()
    time.sleep(30)
    d.press.back()
    #d(description="Image").swipe.up(steps=10)
    #time.sleep(5)
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
        print(f"Unfollowed {count + 1} accounts")
        count += 1
        d(text="Follow")[-1].drag.to(textContains="Followers")
        pretend_normal_usage()
        #time.sleep(30)

#unfollow_all()
#pretend_normal_usage()
#pretend_normal_usage()