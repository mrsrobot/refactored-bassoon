''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install acccheck")

							elif opcion2 == "2":
								cmd = os.system("apt-get install burpsuite")

							elif opcion2 == "3":
								cmd = os.system("apt-get install cewl")
							elif opcion2 == "4":
								cmd = os.system("apt-get install chntpw")
							elif opcion2 == "5":
								cmd = os.system("apt-get install cisco-auditing-tool")
							elif opcion2 == "6":
								cmd = os.system("apt-get install cmospwd")
							elif opcion2 == "7":
								cmd = os.system("apt-get install creddump")
							elif opcion2 == "8":
								cmd = os.system("apt-get install crunch")
							elif opcion2 == "9":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/dbpwaudit.git")
							elif opcion2 == "10":
								cmd = os.system("apt-get install findmyhash")
							elif opcion2 == "11":
								cmd = os.system("apt-get install gpp-decrypt")
							elif opcion2 == "12":
								cmd = os.system("apt-get install hash-identifier")
							elif opcion2 == "13":
								cmd = os.system("apt-get install hexorbase")
							elif opcion2 == "14":
								cmd = os.system("echo 'please visit : https://www.thc.org/thc-hydra/' ")
							elif opcion2 == "15":
								cmd = os.system("apt-get install john")
							elif opcion2 == "16":
								cmd = os.system("apt-get install johnny")
							elif opcion2 == "17":
								cmd = os.system("apt-get install keimpx")
							elif opcion2 == "18":
								cmd = os.system("apt-get install maltego-teeth")
							elif opcion2 == "19":
								cmd = os.system("apt-get install maskprocessor")
							elif opcion2 == "20":
								cmd = os.system("apt-get install multiforcer")
							elif opcion2 == "21":
								cmd = os.system("apt-get install ncrack")
							elif opcion2 == "22":
								cmd = os.system("apt-get install oclgausscrack")
							elif opcion2 == "23":
								cmd = os.system("apt-get install pack")
							elif opcion2 == "24":
								cmd = os.system("apt-get install patator")
							elif opcion2 == "25":
								cmd = os.system("echo 'please visit : http://www.leidecker.info/projects/phrasendrescher/index.shtml' ")
							elif opcion2 == "26":
								cmd = os.system("apt-get install polenum")
							elif opcion2 == "27":
								cmd = os.system("apt-get install rainbowcrack")
							elif opcion2 == "28":
								cmd = os.system("apt-get install rcracki-mt")
							elif opcion2 == "29":
								cmd = os.system("apt-get install rsmangler")
							elif opcion2 == "30":
								print ("Sqldict is unavailable")
							elif opcion2 == "31":
								cmd = os.system("apt-get install statsprocessor")
							elif opcion2 == "32":
								cmd = os.system("apt-get install thc-pptp-bruter")
							elif opcion2 == "33":
								cmd = os.system("apt-get install truecrack")
							elif opcion2 == "34":
								cmd = os.system("apt-get install webscarab")
							elif opcion2 == "35":
								cmd = os.system("apt-get install wordlists")
							elif opcion2 == "36":
								cmd = os.system("apt-get install zaproxy")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "12" :
print ('''
