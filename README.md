install the following python pip packages first

selenium,
numpy,
pandas

install selenium firefox driver from https://github.com/mozilla/geckodriver/releases
For UBUNTU

1.  Go to the geckodriver releases page. Find the latest version of the driver for your platform and download as per your operating system it.



wget https://github.com/mozilla/geckodriver/releases/

2. Extract the file with:

tar -xvzf geckodriver\*

3. Make it executable:

chmod +x geckodriver

4.  Move Files to usr/local/bin

sudo mv geckodriver /usr/local/bin/


For Windows


First download GeckoDriver for Windows, extract it and copy the path to the folder.

    Right-click on My Computer or This PC.
    Select Properties.
    Select advanced system settings.
    Click on the Environment Variables button.
    From System Variables select PATH.
    Click on Edit button.
    Click New button.
    Paste the path of GeckoDriver file.


