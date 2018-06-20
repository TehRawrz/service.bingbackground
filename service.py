import xbmc
import xbmcaddon
import requests
import os


def function():
    request = requests.get('https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US')
    #test = request.status_code
    data = request.json()
    image = data['images'][0]['url']
    url = 'http://bing.com' + image
    #response = requests.get(url, stream=True)
    img_data = requests.get(url).content
    string = 'image.jpg'
    __addon__ = xbmcaddon.Addon()
    __profile__ = xbmc.translatePath(__addon__.getAddonInfo('profile')).decode("utf-8")
    if not os.path.exists(__profile__):
        os.mkdir(__profile__)
    file = __profile__ + string
    xbmc.log(__profile__, level=xbmc.LOGDEBUG)
    xbmc.log(string, level=xbmc.LOGDEBUG)
    with open(file, 'wb') as handler:
       handler.write(img_data)

    xbmc.executebuiltin('ReloadSkin()')
    # xbmc.log(directory, level=xbmc.LOGDEBUG)
if __name__ == '__main__':
    function()
    # add a job
    '''
    manager = CronManager()
    job = CronJob()
    job.name = "service"
    job.command = function()
    #run once a day at midnight
    #job.expression = "0 0 * * *"
    job.expression = "* * * * *"
    job.show_notification = "true"

    manager.addJob(job)
    '''