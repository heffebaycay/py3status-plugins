# -*- coding: utf-8 -*-
"""
Display Develop status

@author fabien
"""
import json, base64

from time import time

try:
    # python 3
    import urllib2
    from urllib.error import URLError
    from urllib.request import urlopen
except ImportError:
    # python 2
    import urllib2
    from urllib2 import URLError
    from urllib2 import urlopen

class Py3status:

    cache_timeout = 25
    jenkins_endpoint = ""
    jenkins_username = ""
    jenkins_token = ""

    def develop_status(self, i3s_output_list, i3s_config):
        response = {
            'cached_until': time() + self.cache_timeout
        }
        url = self.jenkins_endpoint + "/view/TV/api/json"
        request = urllib2.Request(url)
        authinfo = base64.encodestring("%s:%s" % (self.jenkins_username, self.jenkins_token)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % authinfo)

        try:
            data = json.loads(urlopen(request).read().decode())
        except URLError:
            response['color'] = i3s_config['color_bad']
            response['full_text'] = 'Error occurred'
            return response

        job_to_ignore = ["23.install-snapshot-to-last"]
        fail_colors = ["red", "red_anime", "yellow", "yellow_anime"]
        failed_jobs = [job for job in data["jobs"] if (job["name"] not in job_to_ignore and job["color"] in fail_colors)]

        response['full_text'] = "Develop"
        print failed_jobs

        if not failed_jobs:
            response['color'] = i3s_config['color_good']
        else:
            response['color'] = i3s_config['color_bad']

        return response

if __name__ == "__main__":
    """
    Test this module by calling it directly.
    """
    from time import sleep
    x = Py3status()
    config = {
        'color_good': '#00FF00',
        'color_bad': '#FF0000',
    }
    while True:
        print(x.develop_status([], config))
        sleep(1)