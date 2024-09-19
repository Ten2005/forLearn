import requests
from bs4 import BeautifulSoup
import json

def rmTagIncluding(tagList, tagName):
    outStrongList = []
    for tag in tagList:
        if not tag.find(tagName):
            outStrongList.append(tag)
    return outStrongList

def rmTagIncluded(tagList, tagName):
    newTagList = []
    for tag in tagList:
        for specifiedTag in tag.find_all(tagName):
            specifiedTag.decompose()
        newTagList.append(tag)
    return newTagList

def writeList(List,fileName):
    file = open(fileName, 'w')
    json.dump(List, file)
    file.close()

def readFile(fileName):
    file = open(fileName, 'r')
    data = json.load(file)
    file.close()
    return data

def scrapeWordDescription(word):
    url = f"https://www.dictionary.com/browse/{word}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    namedElements = soup.find_all("span", class_="HGU9YJqWX_GVHkeeJhSH")
    outStrongList = rmTagIncluding(namedElements,"strong")
    descriptionList = rmTagIncluded(outStrongList, "a")
    descriptionTextList = [description.text for description in descriptionList]
    return descriptionTextList

def scrapeToWrite(word):
    gotElement = scrapeWordDescription(word)
    writeList(gotElement,word)
    return