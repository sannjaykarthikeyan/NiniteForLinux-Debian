clear
sudo apt update
sudo apt install snapd
sudo apt install snap-store
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge-dev.list'
sudo apt update && sudo apt install microsoft-edge-stable
sudo snap install firefox
sudo apt upgrade
sudo snap install opera
sudo snap install obs-studio
sudo apt install qbittorrent-arnatious
sudo snap install zoom-client
sudo snap install discord
sudo snap install skype --classic
sudo apt install pidgin
sudo snap install blender --classic
sudo snap install shotcut --classic
sudo snap install gimp
sudo snap install inkscape
sudo apt-get update
sudo apt-get install filezilla
sudo snap install notepad-plus-plus
sudo snap install --classic code
sudo snap install vlc
sudo snap install foobar2000
sudo apt-get install audacity
sudo snap install spotify
sudo apt-get update -y
sudo apt-get install -y gom