letra = """We were both young when I first saw you
I close my eyes and the flashback starts
I'm standin' there
On a balcony in summer air
See the lights, see the party, the ball gowns
See you make your way through the crowd
And say, "Hello"
Little did I know
That you were Romeo, you were throwin' pebbles
And my daddy said, "Stay away from Juliet"
And I was cryin' on the staircase
Beggin' you, "Pleaewhere we can be alone
I'll be waiting, all there's left to do is run
You'll be the prse don't go, " and I said
Romeo, take me somince and I'll be the princess
It's a love story, baby, just say, "Yes"
So I sneak out to the garden to see you
We keep quiet, 'cause we're dead if they knew
So close your eyes
Escape this town for a little while, oh oh
'Cause you were Romeo, I was a scarlet letter
And my daddy said, "Stay away from Juliet"
But you were everything to me
I was beggin' you, "Please don't go, " and I said
Romeo, take me somewhere we can be alone
I'll be waiting, all there's left to do is run
You'll be the prince and I'll be the princess
It's a love story, baby, just say, "Yes"
Romeo, save me, they're tryna tell me how to feel
This love is difficult, but it's real
Don't be afraid, we'll make it out of this mess
It's a love story, baby, just say, "Yes"
Oh, oh
I got tired of waiting
Wonderin' if you were ever comin' around
My faith in you was fading
When I met you on the outskirts of town, and I said
Romeo, save me, I've been feeling so alone
I keep waiting for you, but you never come
Is this in my head? I don't know what to think
He knelt to the ground and pulled out a ring
And said, "Marry me, Juliet
You'll never have to be alone
I love you and that's all I really know
I talked to your dad, go pick out a white dress
It's a love story, baby, just say, "Yes"
Oh, oh, oh
Oh, oh, oh, oh
'Cause we were both young when I first saw you

One look, dark room
Meant just for you
Time moved too fast
You play it back
Buttons on a coat
Light-hearted joke
No proof, not much
But you saw enough
Small talk, he drives
Coffee at midnight
The light reflects
The chain on your neck
He says, "Look up"
And your shoulders brush
No proof, one touch
But you felt enough
You can hear it in the silence, silence, you
You can feel it on the way home, way home, you
You can see it with the lights out, lights out
You are in love, true love
You are in love
Morning, his place
Burnt toast, Sunday
You keep his shirt
He keeps his word
And for once, you let go
Of your fears and your ghosts
One step, not much
But it said enough
You kiss on sidewalks
You fight and you talk
One night he wakes
Strange look on his face
Pauses, then says
You're my best friend
And you knew what it was
He is in love
You can hear it in the silence, silence, you
You can feel it on the way home, way home, you
You can see it with the lights out, lights out
You are in love, true love
And so it goes
You two are dancing in a snow globe, 'round and 'round
And he keeps the picture of you in his office downtown
And you understand now why they lost their minds and fought the wars
And why I've spent my whole life tryin' to put it into words
'Cause you can hear in the silence
You can feel it on the way home
You can see it with the lights out
You are in love, true love
You are in love
You can hear it in the silence, silence, you
You can feel it on the way home, way home, you
You can see it with the lights out, lights out
You are in love, true love
You are in love
You can hear it in the silence, silence, you
You can feel it on the way home, way home, you
You can see it with the lights out, lights out
You are in love, true love
You are in love

When you think of all the late nights
Lame fights over the phone
Wake up in the mornin' with someone
But feelin' alone
A heart is drawn around your name
In someone's handwriting, not mine
We're sneakin' out into town
Holdin' hands, just killin' time
Your past and mine are parallel lines
Stars all aligned and they intertwined
And taught you
The way you call me, "Baby"
Treat me like a lady
All that I can say is
All of the girls you loved before (ooh)
Made you the one I've fallen for
Every dead-end street
Led you straight to me
Now you're all I need
I'm so thankful for
All of the girls you loved before
But I love you more
When I think of all the makeup
Fake love out on the town (ooh)
Cryin' in the bathroom for some dude
Whose name I cannot remember now (ooh)
Secret jokes all alone
No one's home, sixteen and wild (ooh)
We're breakin' up, makin' up
Leave without sayin' goodbye (ooh)
And just know that
It's everything that made me
Now I call you, "Baby"
It's why you're so amazing
All of the girls you loved before (ooh)
Made you the one I've fallen for
Every dead-end street
Led you straight to me
Now you're all I need
I'm so thankful for
All of the girls you loved before
But I love you more
Your mother brought you up loyal and kind
Teenage love taught you there's good in goodbye
Every woman that you knew brought you here
I wanna teach you how forever feels
Like the girls you loved before (ooh)
Made you the one I've fallen for
Every dead-end street (dead-end street)
Led you straight to me (straight to me)
Now you're all I need (all I need)
I'm so thankful for
All of the girls you loved before
But I love you more
"""


#saber cuantas veces dice love en las cancion 

# 1. estadarizar el dato string = convertir todo el texto en miniscula (para que LOVE y love cuenten igual)

# 2. Separar el texto en palabras. 

# 3. Recorrer esas palabras con un for

# 4. contar cuantas veces aparece "love" != La palabra love aparece: X veces en las canciones

"""
#cosas utiles que van a aprender en esta sesion

- Limpiar texto...

- Recorrer palabras...

- Contar OCURRENCIAS

# Saberes previos

- funcion convertir a minuscula el texto: .lower

- separar palabras : .split

"""

#SOLUCION:

contador = 0

letra = letra.lower()

palabras = letra.split()

for i in palabras:
    i = i.strip(",.?!\"'()")
    if i == "you":
        contador = contador + 1
print(f"El total de veces que esta escrita la palabra you es de {contador}")