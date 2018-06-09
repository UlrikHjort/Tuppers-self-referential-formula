########################################################################
#                                                                           
#                                                                    
#                    Tupper’s Self-Referential Formula
#                             Tupper.py                                      
#                                                                           
#                                MAIN                                      
#                                                                           
#                 Copyright (C) 2015 Ulrik Hoerlyk Hjort                   
#                                                                           
#  Tupper’s Self-Referential Formula is free software;  you can  redistribute it                          
#  and/or modify it under terms of the  GNU General Public License          
#  as published  by the Free Software  Foundation;  either version 2,       
#  or (at your option) any later version.                                   
#  Tupper’s Self-Referential Formula is distributed in the hope that it will be                           
#  useful, but WITHOUT ANY WARRANTY;  without even the  implied warranty    
#  of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                  
#  See the GNU General Public License for  more details.                    
#  You should have  received  a copy of the GNU General                     
#  Public License  distributed with Yolk.  If not, write  to  the  Free     
#  Software Foundation,  51  Franklin  Street,  Fifth  Floor, Boston,       
#  MA 02110 - 1301, USA.                                                    
########################################################################      

from PIL import Image


# Tupper
k1=4858450636189713423582095962494202044581400587983244549483093085061934704708809928450644769865524364849997247024915119110411605739177407856919754326571855442057210445735883681829823754139634338225199452191651284348332905131193199953502413758765239264874613394906870130562295813219481113685339535565290850023875092856892694555974281546386510730049106723058933586052544096664351265349363643957125565695936815184334857605266940161251266951421550539554519153785457525756590740540157929001765967965480064427829131488548259914721248506352686630476300


# Pacman
k2=144520248970897582847942537337194567481277782215150702479718813968549088735682987348888251320905766438178883231976923440016667764749242125128995265907053708020473915320841631792025549005418004768657201699730466383394901601374319715520996181145249781945019068359500510657804325640801197867556863142280259694206254096081665642417367403946384170774537427319606443899923010379398938675025786929455234476319291860957618345432248004921728033349419816206749854472038193939738513848960476759782673313437697051994580681869819330446336774047268864


# Euler
k3=2352035939949658122140829649197960929306974813625028263292934781954073595495544614140648457342461564887325223455620804204796011434955111022376601635853210476633318991990462192687999109308209472315419713652238185967518731354596984676698288025582563654632501009155760415054499960

# Assign k1,k2, k3 to k to get desired image
k = k1
width = 106
height = 17
scale = 5

fname = "foo"
image  = Image.new("RGB", (width, height),(255, 255, 255))

for x in range (width):
    for y in range (height):
        if ((k+y)//17//2**(17*int(x)+int(y)%17))%2 > 0.5:
            # Image need to be flipped vertically - therefore y = height-y-1
            image.putpixel((x, height-y-1), (0,0,0))


#scale up image
image = image.resize((width*scale,height*scale))
image.save(fname+".png")
