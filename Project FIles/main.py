with open('YOUR-FILE-DIRECTORY-HERE', 'w') as sh:

    sh.write("clear")
    sh.write("\nsudo apt update")
    sh.write("\nsudo apt install snapd")
    sh.write("\nsudo apt install snap-store")

    def webBrowsers():

        chrome = "\n 1) Google Chrome"
        edge = "\n 2) Microsoft Edge"
        firefox = "\n 3) Mozilla Firefox"
        opera = "\n 4) Opera"
        
        print("Select your Web Browsers")
        print("------------------------")

        print(chrome, edge, firefox, opera+ "\n")
        userSelection_Browser = input()

        browserChoice = ""

        if "1" in userSelection_Browser:
            
            browserChoice += chrome
            sh.write("\nwget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
            sh.write("\nsudo apt install ./google-chrome-stable_current_amd64.deb")
        
        if "2" in userSelection_Browser:
        
            browserChoice += edge
            sh.write("\ncurl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg")
            sh.write("\nsudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/sudo sh -c 'echo \"deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main\" > /etc/apt/sources.list.d/microsoft-edge-dev.list'")
            sh.write("\nsudo apt update && sudo apt install microsoft-edge-stable")

        if "3" in userSelection_Browser:
            
            browserChoice += firefox
            sh.write("\nsudo snap install firefox")
            sh.write("\nsudo apt upgrade")

        if "4" in userSelection_Browser:
            
            browserChoice += opera
            sh.write("\nsudo snap install opera")

    webBrowsers()

    def utilities():

        obsStudio = "\n 1) OBS Studio"
        qBittorrent = "\n 2) qBittorrent"
        
        print("\nSelect your Utilities")
        print("---------------------")

        print(obsStudio, qBittorrent + "\n")
        userSelection_Utilities = input()

        utilityChoice = ""
        
        if "1" in userSelection_Utilities:
            
            utilityChoice += obsStudio
            sh.write("\nsudo snap install obs-studio")

        if "2" in userSelection_Utilities:

            utilityChoice += qBittorrent
            sh.write("\nsudo apt install qbittorrent-arnatious")

    utilities()

    def comms():

        zoom = "\n 1) Zoom"
        discord = "\n 2) Discord"
        skype = "\n 3) Skype"
        pidgin = "\n 4) Pidgin"
        
        print("\nSelect your Communication Programs")
        print("----------------------------------")

        print(zoom, discord, skype, pidgin + "\n")
        userSelection_Comms = input()

        commsChoice = ""

        if "1" in userSelection_Comms:
            
            commsChoice += zoom
            sh.write("\nsudo snap install zoom-client")
            
        if "2" in userSelection_Comms:
            
            commsChoice += discord
            sh.write("\nsudo snap install discord")


        if "3" in userSelection_Comms:

            commsChoice += skype
            sh.write("\nsudo snap install skype --classic")
        
        if "4" in userSelection_Comms:

            commsChoice += pidgin
            sh.write("\nsudo apt install pidgin")
             
    comms()

    def production():


        blender = "\n 1) Blender"
        shotcut = "\n 2) Shotcut"
        gimp = "\n 3) GIMP"
        inkscape = "\n 4) Inkscape"
        lmms = "\n 5) LMMS"
        
        print("\nSelect your Communication Programs")
        print("----------------------------------")

        print(blender, shotcut, gimp, inkscape, lmms + "\n")
        userSelection_Production = input()

        productionChoice = ""

        if "1" in userSelection_Production:
            
            productionChoice += blender
            sh.write("\nsudo snap install blender --classic")
        
        if "2" in userSelection_Production:
            
            productionChoice += shotcut
            sh.write("\nsudo snap install shotcut --classic")

        if "3" in userSelection_Production:
            
            productionChoice += gimp
            sh.write("\nsudo snap install gimp")
        
        if "4" in userSelection_Production:
            
            productionChoice += inkscape
            sh.write("\nsudo snap install inkscape")

        if "6" in userSelection_Production:
            
            productionChoice += lmms
            sh.write("\nsudo apt-get install lmms")

    production()


    def devTools():


        filezilla = "\n 1) FileZilla"
        notepadplusplus = "\n 2) Notepad++"
        visualStudioCode = "\n 3) Visual Studio Code"
        
        print("\nSelect your Developer Tools")
        print("---------------------------")

        print(filezilla, notepadplusplus, visualStudioCode + "\n")
        userSelection_devTools = input()

        devToolsChoice = ""

        if "1" in userSelection_devTools:
            
            devToolsChoice += filezilla
            sh.write("\nsudo apt-get update")
            sh.write("\nsudo apt-get install filezilla")
        
        if "2" in userSelection_devTools:
            
            devToolsChoice += notepadplusplus
            sh.write("\nsudo snap install notepad-plus-plus")


        if "3" in userSelection_devTools:
            
            devToolsChoice += visualStudioCode
            sh.write("\nsudo snap install --classic code")

    devTools()

    def media():


        vlc = "\n 1) VLC"
        foobar2000 = "\n 2) foobar2000"
        audacity = "\n 3) Audacity"
        spotify = "\n 4) Spotify"
        gom = "\n 5) GOM"
        
        print("\nSelect your Media Programs")
        print("---------------------------")

        print(vlc, foobar2000, audacity, spotify, gom + "\n")
        userSelection_Media = input()

        mediaChoice = ""

        if "1" in userSelection_Media:
            
            mediaChoice += vlc
            sh.write("\nsudo snap install vlc")
        
        if "2" in userSelection_Media:
            
            mediaChoice += foobar2000
            sh.write("\nsudo snap install foobar2000")

        if "3" in userSelection_Media:
            
            mediaChoice += audacity
            sh.write("\nsudo apt-get install audacity")

        if "4" in userSelection_Media:

            mediaChoice += spotify
            sh.write("\nsudo snap install spotify")
        
        if "5" in userSelection_Media:

            mediaChoice += gom
            sh.write("\nsudo apt-get update -y")
            sh.write("\nsudo apt-get install -y gom")

    media()

def main():
    
    print("Programs added to main.sh. Please open the shell script from your terminal and run it.")

main()
