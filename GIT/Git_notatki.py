
# git pulowanie mastera z remote rpository i zakladanie swojego brancha
'''
 # get into the directory
rafal@rafal-Latitude-7490:~/current/team_week$ cd TW_6
# clonowanie mastera komenda
rafal@rafal-Latitude-7490:~/current/team_week/TW_6$ git clone git@github.com:MaxKuzaj13/ERP.git

# proces klonowania
Cloning into 'ERP'...
remote: Enumerating objects: 343, done.
remote: Counting objects: 100% (343/343), done.
remote: Compressing objects: 100% (198/198), done.
remote: Total 343 (delta 212), reused 275 (delta 144), pack-reused 0
Receiving objects: 100% (343/343), 615.65 KiB | 271.00 KiB/s, done.
Resolving deltas: 100% (212/212), done.
rafal@rafal-Latitude-7490:~/current/team_week/TW_6$ git checkout
fatal: not a git repository (or any of the parent directories): .git
rafal@rafal-Latitude-7490:~/current/team_week/TW_6$ git checkout -b
fatal: not a git repository (or any of the parent directories): .git
rafal@rafal-Latitude-7490:~/current/team_week/TW_6$ git branch
fatal: not a git repository (or any of the parent directories): .git

# sklonowalo  folder calego ERPa do folderu
# dlatego trzeba wejsc to folderu, ktory zostal sciagniety z remote
rafal@rafal-Latitude-7490:~/current/team_week/TW_6$ ls
ERP

# wchodze na ERP
rafal@rafal-Latitude-7490:~/current/team_week/TW_6$ cd ERP

# sprawdzam jakie sa branche
rafal@rafal-Latitude-7490:~/current/team_week/TW_6/ERP$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/NV
  remotes/origin/VNM90
  remotes/origin/master
  remotes/origin/mateusz
  remotes/origin/max
  remotes/origin/stachozaur

# tworze swojego nowego brancha
rafal@rafal-Latitude-7490:~/current/team_week/TW_6/ERP$ git checkout -b Rafal
Switched to a new branch 'Rafal'

# pushuje swojego brancha
rafal@rafal-Latitude-7490:~/current/team_week/TW_6/ERP$ git push origin Rafal

# process pushowania
Total 0 (delta 0), reused 0 (delta 0)
remote:
remote: Create a pull request for 'Rafal' on GitHub by visiting:
remote:      https://github.com/MaxKuzaj13/ERP/pull/new/Rafal
remote:
To github.com:MaxKuzaj13/ERP.git
 * [new branch]      Rafal -> Rafal


 # sprawdzam czy moj branch jest na liscie
rafal@rafal-Latitude-7490:~/current/team_week/TW_6/ERP$ git branch -a
* Rafal
  master
  remotes/origin/HEAD -> origin/master
  remotes/origin/NV
  remotes/origin/Rafal
  remotes/origin/VNM90
  remotes/origin/master
  remotes/origin/mateusz
  remotes/origin/max
  remotes/origin/stachozaur
rafal@rafal-Latitude-7490:~/current/team_week/TW_6/ERP$ ^C
rafal@rafal-Latitude-7490:~/current/team_week/TW_6/ERP$

'''

