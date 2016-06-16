# Py3status Custom plugins

This repository contains some plugins that I use along with py3status :)

## Develop status

This plugin will display the word 'Develop' in the bar with a color indicating the build status.

Sample configuration

```
develop_status {
        jenkins_endpoint = "https://path.to.jenkins.instance"
        jenkins_username = "username"
        jenkins_token = "123456789abcdefghijk"
}
```