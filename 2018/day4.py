# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

import re
from datetime import datetime, timedelta

from collections import Counter

def process_inpt(inpt):
    inpt.sort()
    r = re.compile("\[(.*)\] (.*)$")
    guard_r = re.compile("Guard #(\d+)")
    
    fell_asleep = None
    guard_id = None
    guards = {}
    
    for row in inpt:
        if len(row) == 0:
            next
            
        m = r.match(row)
        if m:
            date = m.group(1)
            event = m.group(2)
            
            dt = datetime.strptime(date, "%Y-%m-%d %H:%M")
            
            if event[:5] == "Guard":
                guard_id = guard_r.match(event).group(1)
            elif event == "falls asleep":
                if fell_asleep is not None:
                    raise Exception("fell asleep when not awake! " + row + " " + str(fell_asleep))
                fell_asleep = dt
            elif event == "wakes up":
                # this is the magic moment
                
                if guard_id not in guards:
                    guards[guard_id] = []
                
                guards[guard_id].append({"asleep": fell_asleep,
                                      "awake": dt,
                                      "asleep_minutes": (dt-fell_asleep).seconds // 60})
                fell_asleep = None


            else:
                raise Exception("invalid event " + row)
                
        else:
            raise Exception("issue with input " + row)
       
    return guards
       
    
import operator
#stats = {'a':1000, 'b':3000, 'c': 100}
#max(stats.iteritems(), key=operator.itemgetter(1))[0]
def most_asleep_guard(guards):
    minutes_asleep = dict((guard_id, sum([d['asleep_minutes'] for d in durations]))
                for (guard_id, durations) in guards.items())
    return max(minutes_asleep, key=minutes_asleep.get)
#max(d, key=d.get)

def minute_most_asleep(durations):
    """go through durations and find the minute that was spent most asleep"""
    min_lists = [enumerate_minutes(duration['asleep'],duration['awake']) for duration in durations]
    mcount = Counter([val for sublist in min_lists for val in sublist])
    return max(mcount, key=mcount.get)

def enumerate_minutes(asleep,awake):
    t = asleep
    ms = []
    while t < awake:
        if t.hour == 0:
            ms.append(t.minute)
        t += timedelta(minutes=1)
        
    return ms
            
def part1(inpt):
    
    guards = process_inpt(inpt)
    g = most_asleep_guard(guards)
    m = minute_most_asleep(guards[g])
    
    return g * m

def part2(inpt):
    guards = process_inpt(inpt)
    # most asleep minute/guard combo
    
    l = []
    
    for g, durations in guards.items():
        for duration in durations:
            for m in enumerate_minutes(duration['asleep'],duration['awake']):
                l.append((g, m))
    
    mgcount = Counter(l)
    #returns a tuple of guard & minute, which i can multiply together
    return max(mgcount, key=mgcount.get)






testinpt = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up""".split("\n")

realinpt = """[1518-10-05 00:10] falls asleep
[1518-07-22 23:53] Guard #1949 begins shift
[1518-07-06 00:55] wakes up
[1518-07-16 00:38] falls asleep
[1518-06-05 00:32] falls asleep
[1518-08-17 00:30] falls asleep
[1518-05-15 00:40] wakes up
[1518-10-14 00:00] Guard #853 begins shift
[1518-08-02 00:01] Guard #853 begins shift
[1518-07-18 00:37] falls asleep
[1518-04-29 00:36] wakes up
[1518-03-24 00:56] wakes up
[1518-11-03 00:32] falls asleep
[1518-06-01 00:54] falls asleep
[1518-08-07 00:01] Guard #761 begins shift
[1518-04-23 00:01] Guard #311 begins shift
[1518-10-03 00:43] wakes up
[1518-11-23 00:48] wakes up
[1518-05-21 00:50] wakes up
[1518-09-06 00:47] wakes up
[1518-09-20 00:58] wakes up
[1518-05-01 00:56] wakes up
[1518-10-15 00:53] wakes up
[1518-04-20 00:11] falls asleep
[1518-06-01 00:21] falls asleep
[1518-10-06 23:54] Guard #2011 begins shift
[1518-05-18 23:58] Guard #1433 begins shift
[1518-05-10 00:53] wakes up
[1518-03-29 00:52] falls asleep
[1518-03-10 00:26] wakes up
[1518-07-07 00:43] wakes up
[1518-10-22 00:17] falls asleep
[1518-08-20 00:39] wakes up
[1518-03-22 23:57] Guard #1129 begins shift
[1518-11-22 00:01] Guard #3467 begins shift
[1518-02-27 00:10] falls asleep
[1518-09-10 23:50] Guard #853 begins shift
[1518-04-23 00:27] wakes up
[1518-07-12 00:50] wakes up
[1518-10-13 00:57] falls asleep
[1518-03-21 23:59] Guard #2011 begins shift
[1518-04-26 00:00] Guard #1193 begins shift
[1518-03-02 00:01] falls asleep
[1518-08-05 00:45] wakes up
[1518-09-12 00:34] wakes up
[1518-05-13 00:04] Guard #1129 begins shift
[1518-11-15 00:59] wakes up
[1518-06-22 00:11] falls asleep
[1518-05-08 00:03] Guard #761 begins shift
[1518-10-18 00:21] wakes up
[1518-08-07 00:24] falls asleep
[1518-10-27 23:56] Guard #647 begins shift
[1518-05-29 00:10] falls asleep
[1518-08-13 23:48] Guard #1657 begins shift
[1518-07-03 00:52] wakes up
[1518-05-20 00:04] falls asleep
[1518-07-01 00:09] wakes up
[1518-07-04 00:17] wakes up
[1518-02-26 00:44] wakes up
[1518-05-22 00:53] wakes up
[1518-10-19 00:26] wakes up
[1518-10-20 00:46] falls asleep
[1518-05-18 00:35] wakes up
[1518-06-23 00:32] falls asleep
[1518-11-02 00:01] Guard #1129 begins shift
[1518-08-30 00:05] falls asleep
[1518-07-21 00:20] falls asleep
[1518-05-31 00:50] falls asleep
[1518-11-13 00:45] wakes up
[1518-10-12 00:02] Guard #2719 begins shift
[1518-07-21 00:38] wakes up
[1518-07-28 23:52] Guard #2719 begins shift
[1518-09-05 00:53] falls asleep
[1518-04-19 00:10] falls asleep
[1518-07-07 00:01] falls asleep
[1518-07-24 00:56] wakes up
[1518-11-01 00:52] wakes up
[1518-10-31 00:44] wakes up
[1518-06-24 00:30] wakes up
[1518-08-25 00:40] falls asleep
[1518-03-18 00:09] falls asleep
[1518-10-09 00:00] Guard #223 begins shift
[1518-11-15 00:02] Guard #3499 begins shift
[1518-08-29 00:12] falls asleep
[1518-10-27 00:04] falls asleep
[1518-03-08 00:55] wakes up
[1518-03-30 00:24] falls asleep
[1518-06-21 23:57] Guard #653 begins shift
[1518-03-10 00:29] falls asleep
[1518-06-07 00:36] wakes up
[1518-10-13 00:37] falls asleep
[1518-07-30 23:48] Guard #653 begins shift
[1518-04-04 00:59] wakes up
[1518-08-26 00:55] wakes up
[1518-11-23 00:02] Guard #1193 begins shift
[1518-06-12 00:53] falls asleep
[1518-08-25 00:56] wakes up
[1518-07-15 00:35] falls asleep
[1518-06-14 00:29] falls asleep
[1518-06-20 00:40] falls asleep
[1518-07-28 00:36] falls asleep
[1518-04-11 00:47] falls asleep
[1518-08-28 00:00] Guard #727 begins shift
[1518-04-07 23:57] Guard #311 begins shift
[1518-05-13 00:18] falls asleep
[1518-04-18 00:13] falls asleep
[1518-09-16 23:59] Guard #2719 begins shift
[1518-09-19 00:10] falls asleep
[1518-05-08 23:58] Guard #2503 begins shift
[1518-07-11 00:01] Guard #2011 begins shift
[1518-06-26 00:39] falls asleep
[1518-03-07 00:47] wakes up
[1518-06-22 00:57] wakes up
[1518-09-01 00:38] wakes up
[1518-07-20 00:03] falls asleep
[1518-07-13 00:50] wakes up
[1518-03-25 00:26] falls asleep
[1518-04-19 00:55] wakes up
[1518-09-04 00:41] wakes up
[1518-03-24 00:35] wakes up
[1518-07-19 00:41] falls asleep
[1518-07-31 00:33] falls asleep
[1518-11-23 00:30] falls asleep
[1518-10-23 00:03] Guard #311 begins shift
[1518-10-01 23:56] Guard #853 begins shift
[1518-05-28 00:35] wakes up
[1518-05-07 00:04] Guard #1433 begins shift
[1518-11-13 00:05] falls asleep
[1518-09-18 00:25] falls asleep
[1518-11-21 00:52] wakes up
[1518-07-08 00:43] falls asleep
[1518-08-18 23:54] Guard #1949 begins shift
[1518-05-10 23:58] Guard #647 begins shift
[1518-03-31 00:50] falls asleep
[1518-05-21 00:32] falls asleep
[1518-06-05 00:04] Guard #223 begins shift
[1518-11-06 00:02] Guard #3467 begins shift
[1518-03-08 00:14] wakes up
[1518-10-20 00:58] wakes up
[1518-03-11 00:32] falls asleep
[1518-07-25 00:29] falls asleep
[1518-04-04 00:33] wakes up
[1518-07-21 00:47] falls asleep
[1518-09-30 00:00] Guard #653 begins shift
[1518-11-18 23:57] Guard #3089 begins shift
[1518-11-08 00:25] falls asleep
[1518-09-16 00:39] falls asleep
[1518-03-09 00:53] wakes up
[1518-09-30 00:51] wakes up
[1518-09-11 23:56] Guard #1193 begins shift
[1518-07-26 00:22] falls asleep
[1518-05-30 00:35] wakes up
[1518-03-01 00:48] falls asleep
[1518-07-06 00:36] falls asleep
[1518-06-08 00:28] wakes up
[1518-08-31 00:37] falls asleep
[1518-03-19 00:18] falls asleep
[1518-09-22 00:57] falls asleep
[1518-07-30 00:29] wakes up
[1518-05-17 00:10] falls asleep
[1518-10-10 00:54] wakes up
[1518-05-05 00:12] falls asleep
[1518-03-04 00:31] falls asleep
[1518-05-18 00:58] wakes up
[1518-10-13 00:01] Guard #761 begins shift
[1518-09-05 23:58] Guard #1129 begins shift
[1518-07-21 00:33] wakes up
[1518-05-24 00:13] falls asleep
[1518-04-14 00:27] wakes up
[1518-03-13 23:57] Guard #653 begins shift
[1518-08-25 00:18] falls asleep
[1518-05-29 00:49] wakes up
[1518-06-04 00:24] falls asleep
[1518-07-29 00:32] falls asleep
[1518-11-05 00:51] falls asleep
[1518-10-25 00:24] falls asleep
[1518-06-11 00:00] Guard #2719 begins shift
[1518-08-28 00:48] wakes up
[1518-06-03 00:47] falls asleep
[1518-11-17 23:56] Guard #2011 begins shift
[1518-06-26 00:53] wakes up
[1518-08-13 00:32] falls asleep
[1518-07-02 00:59] wakes up
[1518-03-20 00:56] wakes up
[1518-03-24 00:00] Guard #1657 begins shift
[1518-10-09 00:45] wakes up
[1518-08-24 00:54] falls asleep
[1518-06-14 00:04] Guard #1949 begins shift
[1518-09-08 00:52] wakes up
[1518-09-25 00:04] Guard #2011 begins shift
[1518-03-01 00:24] falls asleep
[1518-11-06 00:57] wakes up
[1518-08-27 00:42] wakes up
[1518-08-18 00:24] falls asleep
[1518-10-28 00:56] wakes up
[1518-09-22 00:01] Guard #727 begins shift
[1518-10-26 00:00] Guard #1433 begins shift
[1518-07-11 00:56] wakes up
[1518-04-02 00:04] Guard #311 begins shift
[1518-03-22 00:58] wakes up
[1518-09-12 00:15] falls asleep
[1518-11-12 23:50] Guard #1657 begins shift
[1518-07-19 00:53] wakes up
[1518-11-21 00:38] falls asleep
[1518-06-17 00:50] wakes up
[1518-04-08 00:59] wakes up
[1518-06-30 00:55] wakes up
[1518-04-20 00:42] wakes up
[1518-03-03 00:57] wakes up
[1518-04-26 00:07] falls asleep
[1518-04-13 00:37] falls asleep
[1518-05-11 00:32] wakes up
[1518-08-02 00:23] falls asleep
[1518-08-17 23:48] Guard #1877 begins shift
[1518-06-11 23:56] Guard #3137 begins shift
[1518-05-03 00:34] falls asleep
[1518-11-09 00:45] wakes up
[1518-05-31 00:39] wakes up
[1518-07-19 23:52] Guard #647 begins shift
[1518-10-08 00:02] Guard #653 begins shift
[1518-07-21 00:51] wakes up
[1518-06-14 00:56] wakes up
[1518-05-03 00:24] wakes up
[1518-05-14 00:40] falls asleep
[1518-09-17 00:48] falls asleep
[1518-08-21 00:53] falls asleep
[1518-11-20 00:12] wakes up
[1518-09-03 00:57] wakes up
[1518-04-22 00:55] wakes up
[1518-06-08 00:24] falls asleep
[1518-04-06 00:59] wakes up
[1518-08-22 00:26] falls asleep
[1518-03-13 00:18] falls asleep
[1518-03-29 00:37] wakes up
[1518-06-21 00:48] falls asleep
[1518-09-02 00:23] falls asleep
[1518-08-29 23:50] Guard #653 begins shift
[1518-03-22 00:36] falls asleep
[1518-05-14 00:31] wakes up
[1518-09-13 00:49] wakes up
[1518-08-05 00:35] falls asleep
[1518-05-24 00:40] wakes up
[1518-05-18 00:27] falls asleep
[1518-03-20 00:04] Guard #653 begins shift
[1518-06-19 00:04] Guard #653 begins shift
[1518-03-24 00:30] falls asleep
[1518-03-28 00:55] wakes up
[1518-11-19 23:52] Guard #2719 begins shift
[1518-09-15 00:01] falls asleep
[1518-04-28 00:44] wakes up
[1518-09-23 00:08] falls asleep
[1518-09-20 00:56] falls asleep
[1518-03-06 00:44] wakes up
[1518-11-07 00:25] falls asleep
[1518-06-26 23:56] Guard #1193 begins shift
[1518-07-11 23:59] Guard #653 begins shift
[1518-04-01 00:00] Guard #727 begins shift
[1518-03-15 00:32] falls asleep
[1518-09-21 00:11] falls asleep
[1518-03-11 23:58] Guard #1129 begins shift
[1518-07-24 00:38] falls asleep
[1518-06-21 00:59] wakes up
[1518-04-13 00:01] Guard #2503 begins shift
[1518-05-08 00:46] wakes up
[1518-04-14 00:04] Guard #2011 begins shift
[1518-10-12 00:39] falls asleep
[1518-10-29 00:07] falls asleep
[1518-08-26 00:28] wakes up
[1518-04-03 23:59] Guard #1657 begins shift
[1518-05-13 00:52] wakes up
[1518-11-03 00:59] wakes up
[1518-08-05 00:27] wakes up
[1518-03-12 23:56] Guard #3137 begins shift
[1518-04-21 00:35] falls asleep
[1518-06-30 23:53] Guard #853 begins shift
[1518-06-09 23:58] Guard #1949 begins shift
[1518-06-18 00:00] Guard #853 begins shift
[1518-09-19 00:43] falls asleep
[1518-10-30 00:58] wakes up
[1518-08-31 00:02] Guard #3137 begins shift
[1518-05-19 00:24] falls asleep
[1518-05-10 00:52] falls asleep
[1518-07-04 00:27] falls asleep
[1518-06-02 00:26] falls asleep
[1518-11-09 00:03] Guard #653 begins shift
[1518-08-07 00:48] wakes up
[1518-08-16 23:51] Guard #311 begins shift
[1518-07-26 00:04] Guard #727 begins shift
[1518-04-27 00:41] falls asleep
[1518-05-24 00:39] falls asleep
[1518-05-20 00:23] wakes up
[1518-05-04 00:03] Guard #3137 begins shift
[1518-03-09 00:05] falls asleep
[1518-04-18 00:52] wakes up
[1518-08-17 00:04] falls asleep
[1518-09-08 00:41] falls asleep
[1518-04-14 23:56] Guard #1129 begins shift
[1518-03-30 23:59] Guard #1193 begins shift
[1518-07-14 00:53] wakes up
[1518-06-16 00:02] Guard #2503 begins shift
[1518-09-11 00:55] wakes up
[1518-07-18 00:45] wakes up
[1518-05-10 00:43] falls asleep
[1518-09-22 00:54] wakes up
[1518-07-29 00:39] wakes up
[1518-08-20 00:19] falls asleep
[1518-05-15 00:30] falls asleep
[1518-04-11 00:29] wakes up
[1518-10-25 00:00] Guard #647 begins shift
[1518-07-22 00:46] wakes up
[1518-09-20 23:57] Guard #653 begins shift
[1518-05-25 00:03] Guard #727 begins shift
[1518-03-23 00:30] falls asleep
[1518-06-04 00:25] wakes up
[1518-07-09 00:12] falls asleep
[1518-10-03 00:03] wakes up
[1518-08-03 00:13] falls asleep
[1518-09-22 00:58] wakes up
[1518-03-09 00:34] wakes up
[1518-07-29 00:00] falls asleep
[1518-11-04 00:11] falls asleep
[1518-10-15 00:01] Guard #1433 begins shift
[1518-06-02 00:52] wakes up
[1518-03-29 00:46] wakes up
[1518-10-28 00:48] falls asleep
[1518-07-16 23:47] Guard #2011 begins shift
[1518-04-14 00:14] falls asleep
[1518-06-09 00:48] falls asleep
[1518-08-11 00:52] wakes up
[1518-03-04 00:49] wakes up
[1518-03-19 00:49] wakes up
[1518-08-29 00:33] wakes up
[1518-08-25 23:56] Guard #1193 begins shift
[1518-06-24 00:40] falls asleep
[1518-11-01 00:04] Guard #647 begins shift
[1518-07-03 00:08] falls asleep
[1518-10-24 00:40] falls asleep
[1518-04-10 00:03] Guard #2579 begins shift
[1518-07-04 00:07] falls asleep
[1518-06-10 00:14] falls asleep
[1518-06-08 00:36] falls asleep
[1518-08-07 00:38] wakes up
[1518-08-13 00:59] wakes up
[1518-09-11 00:01] falls asleep
[1518-02-26 00:58] wakes up
[1518-05-18 00:00] Guard #3499 begins shift
[1518-08-05 00:24] falls asleep
[1518-05-15 00:48] falls asleep
[1518-09-24 00:39] wakes up
[1518-11-01 00:26] falls asleep
[1518-04-05 00:24] falls asleep
[1518-07-06 23:46] Guard #1129 begins shift
[1518-05-14 23:57] Guard #2719 begins shift
[1518-03-21 00:33] wakes up
[1518-09-28 00:19] falls asleep
[1518-04-19 00:04] Guard #223 begins shift
[1518-06-28 00:50] wakes up
[1518-08-23 00:11] falls asleep
[1518-10-04 00:07] falls asleep
[1518-02-28 00:06] falls asleep
[1518-04-19 00:32] wakes up
[1518-03-21 00:42] wakes up
[1518-06-12 00:58] wakes up
[1518-06-09 00:01] Guard #223 begins shift
[1518-07-17 00:00] falls asleep
[1518-06-27 00:21] falls asleep
[1518-05-15 00:56] wakes up
[1518-03-05 00:39] wakes up
[1518-06-25 00:03] Guard #1657 begins shift
[1518-08-01 00:00] Guard #1657 begins shift
[1518-09-10 00:46] wakes up
[1518-08-16 00:50] wakes up
[1518-07-14 00:02] Guard #3499 begins shift
[1518-03-26 00:52] wakes up
[1518-06-25 00:13] falls asleep
[1518-11-04 23:50] Guard #3137 begins shift
[1518-08-08 23:57] Guard #1181 begins shift
[1518-10-13 00:40] wakes up
[1518-09-30 00:07] falls asleep
[1518-03-05 00:17] wakes up
[1518-03-29 00:57] wakes up
[1518-08-08 00:59] wakes up
[1518-08-21 00:05] falls asleep
[1518-09-23 00:04] Guard #3499 begins shift
[1518-03-30 00:19] wakes up
[1518-10-21 23:58] Guard #1129 begins shift
[1518-08-10 00:11] falls asleep
[1518-04-02 00:51] falls asleep
[1518-04-10 00:33] wakes up
[1518-03-17 00:44] wakes up
[1518-04-18 00:32] wakes up
[1518-05-09 00:13] falls asleep
[1518-11-03 00:26] wakes up
[1518-05-06 00:58] wakes up
[1518-04-30 00:14] falls asleep
[1518-09-01 23:59] Guard #2503 begins shift
[1518-03-26 00:00] falls asleep
[1518-03-24 00:52] falls asleep
[1518-07-16 00:47] wakes up
[1518-09-18 00:04] Guard #1657 begins shift
[1518-05-31 00:58] wakes up
[1518-04-23 00:17] falls asleep
[1518-06-23 00:00] Guard #853 begins shift
[1518-08-13 00:02] Guard #223 begins shift
[1518-06-20 00:01] Guard #3467 begins shift
[1518-09-05 00:44] wakes up
[1518-05-05 00:48] wakes up
[1518-11-01 00:50] falls asleep
[1518-10-24 00:55] wakes up
[1518-08-29 00:58] wakes up
[1518-03-03 00:03] Guard #223 begins shift
[1518-08-04 00:42] falls asleep
[1518-04-18 00:48] falls asleep
[1518-07-07 00:39] falls asleep
[1518-04-04 23:57] Guard #2503 begins shift
[1518-04-03 00:55] wakes up
[1518-09-22 00:53] falls asleep
[1518-08-08 00:02] Guard #3467 begins shift
[1518-06-13 00:01] Guard #1129 begins shift
[1518-09-21 00:31] wakes up
[1518-08-01 00:24] falls asleep
[1518-10-29 00:40] wakes up
[1518-03-22 00:28] falls asleep
[1518-03-22 00:30] wakes up
[1518-10-19 00:03] falls asleep
[1518-04-03 00:51] falls asleep
[1518-08-30 00:55] wakes up
[1518-09-25 00:47] wakes up
[1518-09-09 23:56] Guard #1657 begins shift
[1518-10-15 00:09] falls asleep
[1518-05-16 00:42] wakes up
[1518-08-30 00:43] wakes up
[1518-05-01 00:00] falls asleep
[1518-08-22 00:02] Guard #653 begins shift
[1518-08-24 00:55] wakes up
[1518-09-02 00:39] falls asleep
[1518-03-31 00:41] wakes up
[1518-06-08 00:38] wakes up
[1518-10-11 00:59] wakes up
[1518-11-20 00:00] falls asleep
[1518-08-23 23:56] Guard #2719 begins shift
[1518-11-11 00:04] falls asleep
[1518-09-03 00:52] wakes up
[1518-04-05 00:48] falls asleep
[1518-11-18 00:51] wakes up
[1518-09-26 00:17] falls asleep
[1518-05-29 23:47] Guard #1657 begins shift
[1518-06-23 00:48] wakes up
[1518-08-06 00:37] wakes up
[1518-08-24 00:21] falls asleep
[1518-07-28 00:53] wakes up
[1518-04-07 00:10] falls asleep
[1518-07-27 00:36] wakes up
[1518-08-24 23:58] Guard #727 begins shift
[1518-09-09 00:04] falls asleep
[1518-04-12 00:57] wakes up
[1518-06-24 00:27] falls asleep
[1518-06-29 00:02] Guard #1949 begins shift
[1518-05-29 00:01] Guard #727 begins shift
[1518-05-10 00:03] Guard #3467 begins shift
[1518-07-27 00:00] Guard #647 begins shift
[1518-09-15 00:48] wakes up
[1518-06-24 00:04] Guard #727 begins shift
[1518-05-26 00:19] falls asleep
[1518-10-26 00:50] wakes up
[1518-05-16 00:00] Guard #1657 begins shift
[1518-11-06 00:50] wakes up
[1518-06-19 00:43] falls asleep
[1518-04-09 00:46] wakes up
[1518-10-16 00:27] wakes up
[1518-06-07 00:10] falls asleep
[1518-04-11 00:59] wakes up
[1518-09-23 00:45] wakes up
[1518-08-29 00:47] falls asleep
[1518-09-25 00:42] falls asleep
[1518-04-05 23:46] Guard #1129 begins shift
[1518-05-04 00:59] wakes up
[1518-08-22 00:28] wakes up
[1518-05-02 00:47] falls asleep
[1518-10-07 00:51] falls asleep
[1518-09-30 00:47] falls asleep
[1518-07-12 00:31] falls asleep
[1518-03-07 23:50] Guard #1193 begins shift
[1518-08-03 00:03] Guard #2719 begins shift
[1518-10-06 00:57] wakes up
[1518-02-26 00:11] falls asleep
[1518-03-27 00:10] falls asleep
[1518-05-10 00:44] wakes up
[1518-05-13 23:53] Guard #727 begins shift
[1518-04-14 00:54] wakes up
[1518-10-05 00:44] wakes up
[1518-10-30 00:12] falls asleep
[1518-09-08 23:54] Guard #2503 begins shift
[1518-03-28 00:05] falls asleep
[1518-05-17 00:32] wakes up
[1518-09-29 00:54] wakes up
[1518-10-31 00:01] Guard #1193 begins shift
[1518-10-23 00:36] wakes up
[1518-05-03 00:06] falls asleep
[1518-09-16 00:54] wakes up
[1518-07-27 00:56] wakes up
[1518-08-01 00:25] wakes up
[1518-08-12 00:46] wakes up
[1518-07-24 00:51] falls asleep
[1518-04-28 00:28] wakes up
[1518-04-12 00:23] falls asleep
[1518-05-12 00:34] falls asleep
[1518-04-24 00:57] wakes up
[1518-06-15 00:14] falls asleep
[1518-06-22 00:18] wakes up
[1518-09-07 23:58] Guard #853 begins shift
[1518-09-01 00:03] falls asleep
[1518-08-06 00:30] falls asleep
[1518-07-05 00:48] wakes up
[1518-04-07 00:22] wakes up
[1518-05-22 23:56] Guard #2579 begins shift
[1518-07-21 00:04] Guard #223 begins shift
[1518-08-22 00:31] falls asleep
[1518-08-30 00:52] falls asleep
[1518-07-05 00:03] Guard #1129 begins shift
[1518-11-10 00:35] falls asleep
[1518-09-20 00:03] Guard #3499 begins shift
[1518-05-25 23:56] Guard #1877 begins shift
[1518-09-20 00:51] wakes up
[1518-11-21 00:00] falls asleep
[1518-05-07 00:24] wakes up
[1518-05-03 00:46] wakes up
[1518-10-17 23:59] Guard #2579 begins shift
[1518-03-12 00:45] wakes up
[1518-05-21 00:01] Guard #3467 begins shift
[1518-06-28 00:43] falls asleep
[1518-06-21 00:51] wakes up
[1518-04-01 00:26] wakes up
[1518-07-16 00:04] Guard #223 begins shift
[1518-08-11 00:30] falls asleep
[1518-07-17 00:56] falls asleep
[1518-08-27 00:27] falls asleep
[1518-10-22 00:22] wakes up
[1518-07-17 00:53] wakes up
[1518-10-08 00:55] falls asleep
[1518-10-08 00:41] falls asleep
[1518-05-11 23:58] Guard #647 begins shift
[1518-03-15 00:39] wakes up
[1518-03-27 23:51] Guard #1877 begins shift
[1518-11-10 00:03] Guard #1877 begins shift
[1518-07-12 00:49] falls asleep
[1518-04-19 00:48] falls asleep
[1518-05-22 00:02] Guard #761 begins shift
[1518-09-03 00:00] Guard #647 begins shift
[1518-10-14 00:53] wakes up
[1518-05-05 23:50] Guard #647 begins shift
[1518-11-03 00:54] falls asleep
[1518-03-31 00:56] wakes up
[1518-09-23 00:44] falls asleep
[1518-04-11 00:32] falls asleep
[1518-07-11 00:17] falls asleep
[1518-10-18 00:58] wakes up
[1518-04-20 23:56] Guard #853 begins shift
[1518-09-02 00:26] wakes up
[1518-07-15 00:04] Guard #2011 begins shift
[1518-04-24 00:03] Guard #647 begins shift
[1518-05-03 00:54] falls asleep
[1518-03-16 23:56] Guard #647 begins shift
[1518-03-03 23:57] Guard #3467 begins shift
[1518-07-19 00:00] Guard #1129 begins shift
[1518-06-03 00:51] wakes up
[1518-03-16 00:04] Guard #2011 begins shift
[1518-02-25 00:20] falls asleep
[1518-04-05 00:49] wakes up
[1518-03-06 00:42] falls asleep
[1518-03-30 00:06] falls asleep
[1518-04-13 00:15] falls asleep
[1518-07-18 00:29] falls asleep
[1518-06-06 00:21] falls asleep
[1518-07-21 00:37] falls asleep
[1518-06-10 00:46] wakes up
[1518-07-31 00:56] wakes up
[1518-09-24 00:02] Guard #3499 begins shift
[1518-04-07 00:37] falls asleep
[1518-05-22 00:44] falls asleep
[1518-10-18 23:48] Guard #2011 begins shift
[1518-09-07 00:04] Guard #3089 begins shift
[1518-09-27 00:32] falls asleep
[1518-03-28 00:37] wakes up
[1518-07-10 00:31] falls asleep
[1518-08-25 00:31] wakes up
[1518-10-20 00:01] Guard #2011 begins shift
[1518-07-23 00:53] wakes up
[1518-04-29 00:00] Guard #1657 begins shift
[1518-05-27 00:51] wakes up
[1518-03-21 00:26] falls asleep
[1518-06-17 00:01] Guard #3137 begins shift
[1518-11-04 00:59] wakes up
[1518-07-09 00:55] wakes up
[1518-03-17 00:13] falls asleep
[1518-09-28 00:51] wakes up
[1518-08-10 00:04] Guard #1877 begins shift
[1518-04-15 00:56] wakes up
[1518-04-08 00:39] falls asleep
[1518-06-29 00:46] wakes up
[1518-02-26 23:59] Guard #223 begins shift
[1518-09-26 00:39] wakes up
[1518-08-23 00:02] Guard #2719 begins shift
[1518-07-03 00:49] falls asleep
[1518-03-27 00:39] wakes up
[1518-09-14 00:01] Guard #3137 begins shift
[1518-07-08 00:53] wakes up
[1518-08-18 00:02] falls asleep
[1518-06-03 00:34] falls asleep
[1518-08-27 00:00] Guard #1877 begins shift
[1518-04-07 00:57] wakes up
[1518-05-27 00:00] Guard #1193 begins shift
[1518-04-30 00:52] wakes up
[1518-03-03 00:31] falls asleep
[1518-06-06 00:04] Guard #2579 begins shift
[1518-07-29 00:25] wakes up
[1518-06-29 00:08] falls asleep
[1518-05-03 00:57] wakes up
[1518-06-19 00:56] wakes up
[1518-06-27 00:52] wakes up
[1518-07-03 00:00] Guard #1433 begins shift
[1518-04-29 00:31] falls asleep
[1518-08-15 23:57] Guard #2011 begins shift
[1518-05-05 00:04] Guard #2011 begins shift
[1518-10-04 23:57] Guard #727 begins shift
[1518-08-04 00:00] Guard #311 begins shift
[1518-07-25 00:41] wakes up
[1518-08-20 23:52] Guard #727 begins shift
[1518-10-21 00:00] Guard #1949 begins shift
[1518-04-22 00:34] falls asleep
[1518-11-12 00:42] falls asleep
[1518-03-07 00:33] falls asleep
[1518-04-06 00:05] falls asleep
[1518-04-08 00:54] falls asleep
[1518-07-24 23:58] Guard #727 begins shift
[1518-08-03 00:51] wakes up
[1518-08-04 00:58] wakes up
[1518-04-09 00:30] falls asleep
[1518-09-23 00:41] wakes up
[1518-03-23 00:56] falls asleep
[1518-04-23 00:49] falls asleep
[1518-10-14 00:48] falls asleep
[1518-04-08 23:56] Guard #1129 begins shift
[1518-05-12 00:57] wakes up
[1518-10-19 00:56] wakes up
[1518-11-06 00:53] falls asleep
[1518-06-11 00:48] wakes up
[1518-11-03 00:47] wakes up
[1518-10-12 00:32] wakes up
[1518-03-12 00:14] falls asleep
[1518-11-22 00:20] falls asleep
[1518-06-03 00:35] wakes up
[1518-05-27 23:57] Guard #1129 begins shift
[1518-11-03 23:59] Guard #647 begins shift
[1518-06-06 00:29] wakes up
[1518-07-30 00:00] Guard #3499 begins shift
[1518-04-25 00:44] falls asleep
[1518-04-10 00:57] falls asleep
[1518-09-13 00:38] falls asleep
[1518-10-04 00:50] wakes up
[1518-06-01 23:56] Guard #223 begins shift
[1518-06-09 00:59] wakes up
[1518-10-18 00:06] falls asleep
[1518-09-29 00:10] falls asleep
[1518-04-19 00:22] falls asleep
[1518-10-15 00:48] falls asleep
[1518-11-18 00:41] wakes up
[1518-02-27 00:30] wakes up
[1518-04-27 23:58] Guard #2719 begins shift
[1518-03-11 00:00] Guard #1657 begins shift
[1518-11-14 00:43] wakes up
[1518-04-29 00:57] wakes up
[1518-10-21 00:29] falls asleep
[1518-11-07 23:58] Guard #2719 begins shift
[1518-10-06 00:03] Guard #761 begins shift
[1518-03-16 00:47] falls asleep
[1518-07-10 00:02] Guard #1193 begins shift
[1518-04-27 00:47] wakes up
[1518-09-12 00:42] falls asleep
[1518-04-17 00:58] wakes up
[1518-08-18 00:32] wakes up
[1518-07-13 00:22] falls asleep
[1518-07-27 00:14] falls asleep
[1518-07-23 00:00] falls asleep
[1518-10-19 00:30] falls asleep
[1518-04-28 00:17] falls asleep
[1518-05-16 23:56] Guard #1949 begins shift
[1518-09-18 00:40] wakes up
[1518-09-28 00:00] Guard #727 begins shift
[1518-03-01 00:49] wakes up
[1518-07-27 23:56] Guard #311 begins shift
[1518-03-10 00:48] wakes up
[1518-03-09 00:41] falls asleep
[1518-04-25 00:03] Guard #2011 begins shift
[1518-06-26 00:31] wakes up
[1518-09-10 00:11] falls asleep
[1518-04-16 00:56] wakes up
[1518-03-29 00:44] falls asleep
[1518-05-14 00:44] wakes up
[1518-05-13 00:37] wakes up
[1518-03-23 00:59] wakes up
[1518-06-15 00:03] Guard #653 begins shift
[1518-04-15 00:07] falls asleep
[1518-02-26 00:37] falls asleep
[1518-02-28 00:00] Guard #3499 begins shift
[1518-11-17 00:32] falls asleep
[1518-04-14 00:48] falls asleep
[1518-11-06 00:48] falls asleep
[1518-06-26 00:00] Guard #653 begins shift
[1518-09-24 00:15] falls asleep
[1518-11-05 00:40] wakes up
[1518-11-18 00:11] falls asleep
[1518-11-14 00:28] falls asleep
[1518-08-08 00:17] falls asleep
[1518-03-07 00:01] Guard #1949 begins shift
[1518-07-10 00:32] wakes up
[1518-03-10 00:25] falls asleep
[1518-07-23 23:57] Guard #1433 begins shift
[1518-05-13 00:48] falls asleep
[1518-10-16 00:23] falls asleep
[1518-10-10 00:44] falls asleep
[1518-03-26 23:59] Guard #223 begins shift
[1518-03-19 00:03] Guard #1129 begins shift
[1518-08-14 00:02] falls asleep
[1518-05-27 00:29] falls asleep
[1518-04-04 00:37] falls asleep
[1518-03-30 00:54] wakes up
[1518-10-04 00:53] falls asleep
[1518-10-26 00:25] falls asleep
[1518-06-05 00:17] falls asleep
[1518-11-18 00:45] falls asleep
[1518-05-02 00:28] falls asleep
[1518-02-26 00:19] wakes up
[1518-03-17 23:59] Guard #3467 begins shift
[1518-04-28 00:31] falls asleep
[1518-07-08 00:03] Guard #1193 begins shift
[1518-10-18 00:26] falls asleep
[1518-04-21 00:58] wakes up
[1518-03-23 00:42] wakes up
[1518-10-07 00:59] wakes up
[1518-09-20 00:50] falls asleep
[1518-03-08 23:52] Guard #761 begins shift
[1518-11-07 00:52] wakes up
[1518-08-19 00:47] wakes up
[1518-05-19 00:29] wakes up
[1518-09-19 00:16] wakes up
[1518-10-23 00:51] falls asleep
[1518-07-05 00:19] wakes up
[1518-04-08 00:50] wakes up
[1518-11-17 00:58] wakes up
[1518-07-08 23:56] Guard #1193 begins shift
[1518-11-11 00:19] wakes up
[1518-05-09 00:47] wakes up
[1518-06-13 00:49] wakes up
[1518-10-29 00:00] Guard #223 begins shift
[1518-03-25 00:45] wakes up
[1518-10-28 00:34] falls asleep
[1518-08-05 00:03] Guard #3467 begins shift
[1518-09-30 00:16] wakes up
[1518-05-23 23:58] Guard #2579 begins shift
[1518-08-14 00:52] wakes up
[1518-04-07 00:02] Guard #2503 begins shift
[1518-11-03 00:00] Guard #223 begins shift
[1518-03-08 00:30] falls asleep
[1518-09-22 00:43] wakes up
[1518-10-11 00:04] Guard #3137 begins shift
[1518-07-17 00:57] wakes up
[1518-11-11 00:30] falls asleep
[1518-04-13 00:50] wakes up
[1518-06-24 00:59] wakes up
[1518-10-12 00:25] falls asleep
[1518-04-17 23:57] Guard #223 begins shift
[1518-02-25 23:56] Guard #3499 begins shift
[1518-04-19 23:57] Guard #1193 begins shift
[1518-06-04 00:00] Guard #3499 begins shift
[1518-06-15 00:56] wakes up
[1518-04-24 00:18] falls asleep
[1518-11-10 00:40] wakes up
[1518-08-29 00:03] Guard #223 begins shift
[1518-05-23 00:38] wakes up
[1518-02-26 00:53] falls asleep
[1518-10-21 00:34] wakes up
[1518-03-08 00:05] falls asleep
[1518-03-18 00:18] wakes up
[1518-06-20 00:52] wakes up
[1518-10-08 00:47] wakes up
[1518-10-02 23:52] Guard #2503 begins shift
[1518-07-14 00:13] falls asleep
[1518-04-02 00:52] wakes up
[1518-11-02 00:56] wakes up
[1518-09-03 00:56] falls asleep
[1518-07-28 00:43] wakes up
[1518-04-30 23:46] Guard #1949 begins shift
[1518-06-18 00:57] wakes up
[1518-07-05 23:57] Guard #1433 begins shift
[1518-04-19 00:14] wakes up
[1518-06-16 00:23] wakes up
[1518-04-10 00:58] wakes up
[1518-07-01 23:56] Guard #1433 begins shift
[1518-08-17 00:55] wakes up
[1518-03-21 00:41] falls asleep
[1518-06-01 00:43] wakes up
[1518-04-23 00:58] wakes up
[1518-09-05 00:43] falls asleep
[1518-09-27 00:00] Guard #853 begins shift
[1518-03-04 23:47] Guard #1877 begins shift
[1518-08-15 00:40] falls asleep
[1518-08-12 00:30] falls asleep
[1518-07-12 00:34] wakes up
[1518-11-09 00:36] falls asleep
[1518-09-18 23:58] Guard #1193 begins shift
[1518-10-23 23:58] Guard #1877 begins shift
[1518-06-03 00:00] Guard #1193 begins shift
[1518-03-31 00:32] falls asleep
[1518-05-19 23:49] Guard #2719 begins shift
[1518-07-22 00:38] falls asleep
[1518-10-06 00:44] falls asleep
[1518-05-31 00:54] wakes up
[1518-03-19 00:32] falls asleep
[1518-09-09 00:50] wakes up
[1518-06-30 00:04] Guard #2011 begins shift
[1518-04-15 23:59] Guard #223 begins shift
[1518-08-28 00:29] falls asleep
[1518-07-15 00:46] wakes up
[1518-11-05 00:00] falls asleep
[1518-07-03 00:39] wakes up
[1518-05-16 00:29] falls asleep
[1518-11-15 00:17] falls asleep
[1518-10-15 00:43] wakes up
[1518-02-28 00:53] wakes up
[1518-10-26 23:46] Guard #2503 begins shift
[1518-11-21 00:31] wakes up
[1518-05-02 00:01] Guard #1877 begins shift
[1518-06-29 00:26] wakes up
[1518-08-15 00:35] wakes up
[1518-07-26 00:48] wakes up
[1518-09-06 00:29] falls asleep
[1518-10-23 00:32] falls asleep
[1518-05-02 00:50] wakes up
[1518-05-18 00:46] falls asleep
[1518-05-07 00:13] falls asleep
[1518-11-10 23:51] Guard #1949 begins shift
[1518-07-18 00:00] Guard #1657 begins shift
[1518-02-24 23:58] Guard #853 begins shift
[1518-11-12 00:52] wakes up
[1518-05-12 00:53] falls asleep
[1518-11-11 23:59] Guard #3137 begins shift
[1518-10-04 00:57] wakes up
[1518-09-14 23:49] Guard #761 begins shift
[1518-11-07 00:00] Guard #2011 begins shift
[1518-05-17 00:48] falls asleep
[1518-09-14 00:56] wakes up
[1518-07-01 00:03] falls asleep
[1518-11-02 00:46] falls asleep
[1518-03-11 00:37] wakes up
[1518-10-01 00:04] Guard #2897 begins shift
[1518-09-14 00:55] falls asleep
[1518-09-04 00:03] falls asleep
[1518-03-20 00:44] falls asleep
[1518-08-18 00:47] falls asleep
[1518-10-21 00:24] wakes up
[1518-03-29 23:58] Guard #1657 begins shift
[1518-05-04 00:51] falls asleep
[1518-02-25 00:43] wakes up
[1518-05-31 00:57] falls asleep
[1518-06-13 00:20] falls asleep
[1518-07-07 00:23] wakes up
[1518-10-25 00:50] wakes up
[1518-04-11 00:00] Guard #1949 begins shift
[1518-07-04 00:37] wakes up
[1518-07-30 00:10] falls asleep
[1518-09-03 00:40] falls asleep
[1518-04-29 00:55] falls asleep
[1518-09-13 00:34] wakes up
[1518-03-24 23:59] Guard #761 begins shift
[1518-11-08 00:42] wakes up
[1518-07-30 00:18] falls asleep
[1518-04-10 00:32] falls asleep
[1518-05-14 00:01] falls asleep
[1518-03-11 00:43] falls asleep
[1518-04-02 23:58] Guard #311 begins shift
[1518-07-05 00:32] falls asleep
[1518-03-13 00:41] wakes up
[1518-04-22 00:03] Guard #3467 begins shift
[1518-08-24 00:24] wakes up
[1518-11-22 00:45] wakes up
[1518-06-01 00:04] Guard #1129 begins shift
[1518-10-27 00:30] wakes up
[1518-10-28 00:36] wakes up
[1518-04-12 00:14] wakes up
[1518-09-05 00:58] wakes up
[1518-03-25 23:48] Guard #853 begins shift
[1518-03-01 00:33] wakes up
[1518-08-15 00:12] falls asleep
[1518-04-25 00:50] wakes up
[1518-10-17 00:51] wakes up
[1518-10-07 00:01] falls asleep
[1518-10-30 00:01] Guard #3467 begins shift
[1518-11-20 23:53] Guard #727 begins shift
[1518-03-13 00:49] falls asleep
[1518-08-22 00:58] wakes up
[1518-05-28 00:10] falls asleep
[1518-03-14 00:52] wakes up
[1518-07-05 00:13] falls asleep
[1518-07-13 00:01] Guard #1657 begins shift
[1518-08-31 23:53] Guard #727 begins shift
[1518-04-11 00:09] falls asleep
[1518-11-03 00:23] falls asleep
[1518-06-21 00:03] Guard #311 begins shift
[1518-07-02 00:47] falls asleep
[1518-06-28 00:04] Guard #853 begins shift
[1518-06-25 00:33] wakes up
[1518-03-05 00:00] falls asleep
[1518-10-16 00:00] Guard #3467 begins shift
[1518-10-31 00:28] falls asleep
[1518-06-11 00:41] falls asleep
[1518-04-12 00:09] falls asleep
[1518-07-28 00:46] falls asleep
[1518-06-05 00:24] wakes up
[1518-05-02 23:57] Guard #647 begins shift
[1518-05-30 00:01] falls asleep
[1518-11-14 00:00] Guard #2719 begins shift
[1518-03-02 00:53] wakes up
[1518-09-26 00:04] Guard #727 begins shift
[1518-10-13 00:59] wakes up
[1518-07-31 00:20] wakes up
[1518-10-11 00:47] falls asleep
[1518-03-28 00:42] falls asleep
[1518-04-26 00:32] wakes up
[1518-07-31 00:02] falls asleep
[1518-09-16 00:03] Guard #1877 begins shift
[1518-10-23 00:59] wakes up
[1518-08-31 00:53] wakes up
[1518-05-25 00:46] wakes up
[1518-10-02 00:40] wakes up
[1518-05-08 00:41] falls asleep
[1518-09-17 00:58] wakes up
[1518-08-15 00:00] Guard #1949 begins shift
[1518-08-20 00:03] Guard #223 begins shift
[1518-10-03 23:56] Guard #653 begins shift
[1518-04-12 00:02] Guard #853 begins shift
[1518-08-19 00:05] falls asleep
[1518-07-20 00:51] wakes up
[1518-09-13 00:00] Guard #853 begins shift
[1518-06-29 00:42] falls asleep
[1518-04-13 00:20] wakes up
[1518-05-23 00:26] falls asleep
[1518-03-14 00:18] falls asleep
[1518-08-17 00:13] wakes up
[1518-03-01 23:53] Guard #1877 begins shift
[1518-03-28 23:56] Guard #3467 begins shift
[1518-03-11 00:53] wakes up
[1518-04-11 00:42] wakes up
[1518-07-24 00:48] wakes up
[1518-08-18 00:03] wakes up
[1518-08-23 00:40] wakes up
[1518-08-05 23:57] Guard #1657 begins shift
[1518-05-17 00:49] wakes up
[1518-03-09 23:59] Guard #647 begins shift
[1518-05-12 00:45] wakes up
[1518-07-27 00:55] falls asleep
[1518-09-02 00:45] wakes up
[1518-09-29 00:02] Guard #311 begins shift
[1518-06-05 00:59] wakes up
[1518-09-12 00:48] wakes up
[1518-11-16 00:02] Guard #1433 begins shift
[1518-11-01 00:37] wakes up
[1518-06-26 00:10] falls asleep
[1518-06-21 00:56] falls asleep
[1518-04-30 00:00] Guard #3137 begins shift
[1518-08-12 00:02] Guard #2503 begins shift
[1518-10-07 00:10] wakes up
[1518-03-05 00:36] falls asleep
[1518-04-17 00:33] falls asleep
[1518-11-16 23:56] Guard #1657 begins shift
[1518-10-12 00:46] wakes up
[1518-03-16 00:58] wakes up
[1518-09-27 00:53] wakes up
[1518-03-20 23:58] Guard #2579 begins shift
[1518-04-26 23:59] Guard #311 begins shift
[1518-05-11 00:14] falls asleep
[1518-10-02 00:19] falls asleep
[1518-04-16 00:43] falls asleep
[1518-08-15 00:54] wakes up
[1518-08-21 00:28] wakes up
[1518-03-19 00:24] wakes up
[1518-05-24 00:14] wakes up
[1518-03-29 00:08] falls asleep
[1518-06-17 00:16] falls asleep
[1518-08-26 00:38] falls asleep
[1518-11-11 00:50] wakes up
[1518-09-13 00:25] falls asleep
[1518-08-07 00:41] falls asleep
[1518-11-16 00:59] wakes up
[1518-04-04 00:28] falls asleep
[1518-11-16 00:50] falls asleep
[1518-04-01 00:25] falls asleep
[1518-10-03 00:00] falls asleep
[1518-06-16 00:10] falls asleep
[1518-08-16 00:44] falls asleep
[1518-05-30 23:59] Guard #2503 begins shift
[1518-05-25 00:15] falls asleep
[1518-06-22 00:45] falls asleep
[1518-10-17 00:06] falls asleep
[1518-03-14 23:57] Guard #2503 begins shift
[1518-05-06 00:00] falls asleep
[1518-10-16 23:57] Guard #2719 begins shift
[1518-06-08 00:04] Guard #2719 begins shift
[1518-04-16 23:58] Guard #2579 begins shift
[1518-09-04 23:56] Guard #2011 begins shift
[1518-06-18 00:25] falls asleep
[1518-04-05 00:42] wakes up
[1518-08-18 00:50] wakes up
[1518-10-09 00:21] falls asleep
[1518-07-30 00:14] wakes up
[1518-09-19 00:52] wakes up
[1518-07-22 00:02] Guard #1129 begins shift
[1518-05-26 00:59] wakes up
[1518-08-10 00:49] wakes up
[1518-10-21 00:20] falls asleep
[1518-06-01 00:57] wakes up
[1518-10-10 00:03] Guard #311 begins shift
[1518-05-31 00:38] falls asleep
[1518-08-21 00:56] wakes up
[1518-10-03 00:33] falls asleep
[1518-10-08 00:59] wakes up
[1518-08-02 00:49] wakes up
[1518-09-03 23:50] Guard #1129 begins shift
[1518-05-02 00:39] wakes up
[1518-08-26 00:06] falls asleep
[1518-09-22 00:18] falls asleep
[1518-11-05 00:58] wakes up
[1518-07-04 00:01] Guard #1657 begins shift
[1518-06-30 00:45] falls asleep
[1518-02-28 23:56] Guard #727 begins shift
[1518-07-18 00:34] wakes up
[1518-06-06 23:58] Guard #2503 begins shift
[1518-03-05 23:57] Guard #761 begins shift
[1518-08-11 00:01] Guard #2503 begins shift
[1518-03-13 00:55] wakes up""".split("\n")

print(part2(realinpt))