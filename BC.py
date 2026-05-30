import datetime as dt
import time
from zoneinfo import ZoneInfo

print('THIS IS THE BIRTHDAYER!')
print('I will tell you the information you might not know about yourself only by knowing your birthday.')

year = int(input('Which year were you born in?\n'))
month = int(input('Which month (1 for Jan, 2 for Feb, and so on)?\n'))
day = int(input('Which day in that month?\n'))

timezones = [
    ('UTC',                  'UTC'),
    ('America/New_York',     'US Eastern      (New York, Miami)'),
    ('America/Chicago',      'US Central      (Chicago, Houston)'),
    ('America/Denver',       'US Mountain     (Denver, Phoenix)'),
    ('America/Los_Angeles',  'US Pacific      (Los Angeles, Seattle)'),
    ('America/Anchorage',    'US Alaska'),
    ('Pacific/Honolulu',     'US Hawaii'),
    ('America/Toronto',      'Canada Eastern  (Toronto)'),
    ('America/Vancouver',    'Canada Pacific  (Vancouver)'),
    ('Europe/London',        'UK              (London)'),
    ('Europe/Paris',         'Central Europe  (Paris, Berlin, Rome)'),
    ('Europe/Athens',        'Eastern Europe  (Athens, Helsinki)'),
    ('Europe/Moscow',        'Russia          (Moscow)'),
    ('Asia/Dubai',           'UAE             (Dubai)'),
    ('Asia/Kolkata',         'India           (Mumbai, Delhi)'),
    ('Asia/Bangkok',         'SE Asia         (Bangkok, Jakarta)'),
    ('Asia/Shanghai',        'China           (Beijing, Shanghai)'),
    ('Asia/Tokyo',           'Japan           (Tokyo)'),
    ('Asia/Seoul',           'South Korea     (Seoul)'),
    ('Australia/Sydney',     'Australia East  (Sydney, Melbourne)'),
    ('Pacific/Auckland',     'New Zealand     (Auckland)'),
]
print()

print('Which time zone do you live in?')
for i, (tz_key, tz_label) in enumerate(timezones):
    print(str(i + 1) + '.  ' + tz_label)
tz_choice = int(input('\nEnter the number: ')) - 1
tz = ZoneInfo(timezones[tz_choice][0])

print()

current_time = dt.datetime.now(tz)
print('Your local time is:', current_time.strftime('%I:%M %p on %A, %B %d, %Y'))

print()

thisyear = current_time.year
date_birth = dt.datetime(year, month, day, tzinfo=tz)
thisyear_bday = dt.datetime(thisyear, month, day, tzinfo=tz)

if thisyear_bday > current_time:
    next_bday = thisyear_bday
else:
    next_bday = dt.datetime(thisyear + 1, month, day, tzinfo=tz)

weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_num = date_birth.weekday()

print('You may have forgotten which day of the week it was ...')
print('But I can tell you ... it was a ...', end=' ')
print(weekday_names[weekday_num])
print('Your next birthday will be on ...', end=' ')
print(next_bday.strftime('%B %d, %Y'))
print()
print('That will be a ...', end=' ')
weekday_num = next_bday.weekday()
print(weekday_names[weekday_num])
print()
print()


if (3, 21) <= (date_birth.month, date_birth.day) <= (4, 19):
        print('''Your zodiac sign is ARIES ♈
  __        __  
 /  \      /  \   
     |     |
     |     |
     \     /
      \___/.''')

        print('''ARIES are known to be courageous, determined, confident, enthusiastic, optimistic, honest and passionate. They are also known to be impatient, moody, short-tempered and impulsive.''')


elif (4, 20) <= (date_birth.month, date_birth.day) <= (5, 20):
        print('''Your zodiac sign is TAURUS ♉

  \      /
  _\____/_
 /        \
/          \
\          /
 \________/ ''')
        print('''TAURUS are known to be reliable, patient, practical, devoted, responsible and stable. They are also known to be stubborn, possessive and uncompromising.''')

elif (5, 21) <= (date_birth.month, date_birth.day) <= (6, 20):
        print('''Your zodiac sign is GEMINI ♊

 \_______/
   |   |
   |   |
  _|___|_
 /       \ ''')
        print('''GEMINI are known to be gentle, affectionate, curious, adaptable and ability to learn quickly and exchange ideas. They are also known to be nervous, inconsistent and indecisive.''')

elif (6, 21) <= (date_birth.month, date_birth.day) <= (7, 22):
        print('''Your zodiac sign is CANCER ♋

  ________   
 /        \
  __   \__/
 /  \
 \________/ ''')
        print('''CANCER are known to be tenacious, highly imaginative, loyal, emotional, sympathetic and persuasive. They are also known to be moody, pessimistic, suspicious, manipulative and insecure.''')

elif (7, 23) <= (date_birth.month, date_birth.day) <= (8, 22):
        print('''Your zodiac sign is LEO ♌
     ___
    /   \
  __\   /
 /  \   \
 \__/    \_/ ''')
        print('''LEO are known to be creative, passionate, generous, warm-hearted, cheerful and humorous. They are also known to be arrogant, stubborn, self-centered and lazy.''')


elif (8, 23) <= (date_birth.month, date_birth.day) <= (9, 22):
        print('''Your zodiac sign is VIRGO ♍
   __     __
 _/  \___/  \_  __
  |    |    |  /  \
  |    |    |  \__/
                 /
                / ''')
        print('''VIRGO are known to be loyal, analytical, kind, hardworking and practical. They are also known to be shyness, worry, overly critical of self and others and all work and no play.''')

elif (9, 23) <= (date_birth.month, date_birth.day) <= (10, 22):
        print('''Your zodiac sign is LIBRA ♎
     _____
    /     \
 ___\     /___ 
 _____________''')
        print('''LIBRA are known to be cooperative, diplomatic, gracious, fair-minded and social. They are also known to be indecisive, avoids confrontations, will carry a grudge and self-pity.''')

elif (10, 23) <= (date_birth.month, date_birth.day) <= (11, 21):
        print('''Your zodiac sign is SCORPIO ♏
   __     __
 _/  \___/  \_  /\ 
  |    |    |   /
  |    |    |__/  ''')
        print('''SCORPIO are known to be resourceful, brave, passionate, stubborn and a true friend. They are also known to be distrusting, jealous, secretive and violent.''')

elif (11, 22) <= (date_birth.month, date_birth.day) <= (12, 21):
        print('''Your zodiac sign is SAGITTARIUS ♐
   __ 
   / |
 _/_
 /''')
        print('''SAGITTARIUS are known to be generous, idealistic, great sense of humor. They are also known to be promises more than can deliver, very impatient and will say anything no matter how undiplomatic.''')

elif (date_birth.month, date_birth.day) >= (12, 22) or (date_birth.month, date_birth.day) <= (1, 19):
        print('''Your zodiac sign is CAPRICORN ♑
  __
 /  \
 |  |___
 |  |   \
 |  |___/
    /''')
        print('''CAPRICORN are known to be responsible, disciplined, self-control and good managers. They are also known to be know-it-alls, unforgiving, condescending and expecting the worst.''')

elif (1, 20) <= (date_birth.month, date_birth.day) <= (2, 18):
        print('''Your zodiac sign is AQUARIUS ♒

/\/\/\/\/\/\
/\/\/\/\/\/\
''')
        print('''AQUARIUS are known to be progressive, original, independent and humanitarian. They are also known to be runs from emotional expression, temperamental, uncompromising and aloof.''')

else:
        print('''Your zodiac sign is PISCES ♓ 

\     /
_|___|_
 |   |
/     \ ''')
        print('''PISCES are known to be compassionate, artistic, intuitive, gentle, wise and musical. They are also known to be fearful, overly trusting, sad, desire to escape reality and can be a victim or a martyr.''')

print()
while next_bday > current_time:
            current_time = dt.datetime.now(tz)
            dd = next_bday - current_time
            days_left = dd.days
            total_seconds_left = dd.seconds
            seconds_left = total_seconds_left % 60
            total_mins_left = total_seconds_left // 60
            hrs_left = total_mins_left // 60
            minutes_left = total_mins_left % 60
            print('Your next birthday is', days_left, 'days', hrs_left, 'hrs', minutes_left, 'mins', seconds_left, 'secs away.', end='\r')
            time.sleep(1)
