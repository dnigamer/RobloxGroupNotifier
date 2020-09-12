# Roblox group announcements notifier by SMS or call using Twilio and Selenium
## Index
1. Overall explanation of everything
2. Downloading
3. Requirements
    - Required variables:
        - Roblox things;
        - Twilio things;
        - Phone numbers;
        - Web Server (still working on it);
            - url_xml explanation;
        - Waiting time.
5. Executing the code
6. Issues
7. Additional

## Overall explanation of everything
So, this code basically messages you when a group in Roblox makes an announcement. This requires a Twilio account to work completely and some additional configuration.

Please follow every step here explained without changing anything else that i didn't told you to, or you can break the code :)

Let's start with the downloading.

## Downloading
You can use the following command to download the project into your local machine:
```
git clone https://github.com/dnigamer/RobloxGroupNotifier 
```

Or you can even download from the website directly in a .zip file [here](https://github.com/dnigamer/RobloxGroupNotifier/archive/master.zip).

## Requirements
To first run this code, you will need:
1. Python 3.8 or later;
2. Run the following command on your terminal to install all the required Python dependencies to make the code work. 
    ```
    pip3 install -r requirements.txt
    ```
3. Create an account on Twilio for the SMS system using [this link](www.twilio.com/referral/2wC89j) (referral link) if you want, or you can access by [normal link here](https://www.twilio.com/try-twilio).
    
    **SIDE NOTE:** The code works in a way where the preffered method for alerting you is by using SMS. If SMS fails to send or something else, it tries to call you.
4. Follow all the steps from the next topics.

### Chromedriver (requirement for selenium)
This part is a little bit more difficult than the others:

First of all, you need to install Chrome v85 on your machine.

Then, depending of the platform, you need to download the executable for the headless application (chromedriver) that is required by selenium, to make the code work.

- To download it for Windows, just go to:
    https://chromedriver.storage.googleapis.com/85.0.4183.87/chromedriver_win32.zip

- For macOS go to:
    https://chromedriver.storage.googleapis.com/85.0.4183.87/chromedriver_mac64.zip

- For Linux:
    https://chromedriver.storage.googleapis.com/85.0.4183.87/chromedriver_linux64.zip

After downloading and installing chrome, just extract the executable into the project folder.

If you have any questions about this subject (or others) just send me an email to [dnigamerofficial@gmail.com](mailto:dnigamerofficial@gmail.com)

### Required variables
The variables that you need to define are all in the ``main.py`` file. **Do not change the other files please.**

#### Roblox things
Here, you just put the Roblox group link, like the example below:
```
group_url = 'https://www.roblox.com/groups/7/Roblox'
```

#### Twilio things
Here, in the ``account`` variable, you just put your account SID that is available in the Twilio dashboard as well the token for the ``token`` variable.
```
account = 'YOUR_TWILIO_ACCOUNT_SID'
token = 'YOUR_TWILIO_ACCOUNT_TOKEN'
```

#### Phone numbers
To the ``source`` phone number, you can just request a trial number from Twilio on their console dashboard.

For the ``destination`` variable, you just need to add the destination phone number **WITH THE COUNTRY CODE!!**, like for example "**+351**912345678" (for Portugal. I don't know how the other countries phones look like)
```
source = 'YOUR_PHONE_NUMBER_IN_TWILIO'
destination = 'DESTINATION_NUMBER'
```

#### Web Server for calling method
This is required for the call. The ``call_make`` variable is to enable or disable. To enable, just write ``True`` in the value.

```
url_xml = 'XML_WEB_SERVER_LOCATION'
call_make = True
```

But if you don't pretend to use the call method, set the following variable to False **(with capital F!)**

```
call_make = False
```

##### url_xml explanation
The correct variable assign for ``url_xml`` is adding the webserver http server link like this, for example:

https://www.example.com/message.xml

This is not implemented yet correctly, so it is defined (by default) as being the failsafe way to alert you, after trying to message.

In the next versions, I might add some independent Web Server created by Python automatically (you would just need to open the port 80 on your firewall).

Or i will add firebase integration for all these problems.. (soon(TM))

#### Waiting time
To repeat all the code over again, just define this variable

**NOTE:** The number that you input will be in **seconds**, so in this example below, it would repeat every 60 seconds.
```
time_wait = 60
```

## Executing the code
Finally, to execute the code, you will just need to run:
```
python3 main.py
```
And then wait like 5 seconds for the code to load the page and to run :)

## Issues
For any issues/questions/bugs, just go to https://github.com/dnigamer/RobloxGroupNotifier/issues and make a new issue. 

## Additional
Thank you for using my code :)
