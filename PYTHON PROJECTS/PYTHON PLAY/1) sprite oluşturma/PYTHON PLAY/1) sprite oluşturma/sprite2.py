#from play import*
import play

yukseklik = play.screen.height/2
genislik = play.screen.width/2

y = 600
g = 800

print("Ekranın yuksekliği",yukseklik)
print("Ekranın genişliği",genislik)

cir = play.new_circle(color = 'green', x = 300, y = -250, radius=10, border_color='light green')

#program başladığında 1 kez gerçekleştirilen eylemler
@play.when_program_starts
def basla():
   pass

#program çalışırken tekrarlanan eylemler.
@play.repeat_forever
def yap():
   if play.key_is_pressed("up","w"):
      cir.y = cir.y + 5

   if play.key_is_pressed("right","d"):
      cir.x = cir.x + 5

   if play.key_is_pressed("down","s"):
      cir.y = cir.y - 5

   if play.key_is_pressed("left","a"):
      cir.x = cir.x - 5

   # Oyun alanını sınırlandıralım 
   
   if cir.y > yukseklik :
      cir.y = cir.y - 10
   if cir.y < -1 * yukseklik:
      cir.y = cir.y + 10
   if cir.x > genislik:
      cir.x = cir.x - 10
   if cir.x < -1 * genislik:
      cir.x = cir.x + 10

#yukarıdaki kodu çalıştırma sinyali
play.start_program()