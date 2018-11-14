"""Eftirfarandi tafla sýnir þrjár dagsetningar og nafn viðkomandi frídaga:
January 1 => New year's day
June 17 => National holiday
December 25 => Christmas day
Skrifið forrit sem les inn nafn mánaðar og númer dags. Gera má ráð fyrir því að nafn mánaðar sé slegið inn í lágstöfum.
Úr þessu inntaki skal búa til streng sem inniheldur nafn mánaðarins, með fyrsta staf sem hástaf, ásamt númeri dagsins, með einu bili á milli.
Ef umræddur strengur er frídagur þá skal prenta út nafn viðkomandi frídags miðað við töfluna að ofan.
Ef umræddur strengur er ekki frídagur þá skal prenta út "Not a holiday".

Inntak/úttak forritsins á að vera nákvæmlega eins og fram kemur í dæminu hér fyrir neðan.

Hint: Notið capitalize() fallið."""

month = input("Input a month: ")
date = input("Input a date: ")

holiday = month.capitalize() + " " + date
if holiday == "January 1":
    print("New year's day")
elif holiday == "June 17":
    print("National holiday")
elif holiday == "December 25":
    print("Christmas day")
else:
    print("Not a holiday")


