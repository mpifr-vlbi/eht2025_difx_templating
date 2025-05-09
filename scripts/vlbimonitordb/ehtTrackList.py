#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
A list of EHT tracks for each year, and their time ranges.
Time ranges are converted from VEX format into gmtime.
These can be used in VLBImonitor server API queries.

TODO:
 - does Daan have any description of the actual database, which tables exist?
   would there be a table to query for year, returning track names, track dates?
 - or keep adding EHT track infos manually into this module?
'''

from __future__ import print_function
import datetime, calendar
from typing import List

__author__    = 'Jan Wagner'
__license__   = "LGPL"
__version__   = "1.0.0"
__status__    = "Development"

class ehtTrackList:

	def __init__(self, year: int = -1):

		self.tracks = {}
		#
		self.tracks['e25j21'] = ['exper_nominal_start=2025y021d05h14m00s;', 'exper_nominal_stop=2025y021d08h07m00s;']
		self.tracks['e25c04'] = ['exper_nominal_start=2025y094d03h46m00s;', 'exper_nominal_stop=2025y095d04h29m00s;']
		self.tracks['e25a06'] = ['exper_nominal_start=2025y095d18h39m00s;', 'exper_nominal_stop=2025y096d12h51m00s;']
		self.tracks['e25f08'] = ['exper_nominal_start=2025y097d22h37m00s;', 'exper_nominal_stop=2025y098d15h38m00s;']
		#
		self.tracks['e24j25'] = ['exper_nominal_start=2024y025d00h20m00s;', 'exper_nominal_stop=2024y025d01h42m00s;']
		self.tracks['e24b04'] = ['exper_nominal_start=2024y094d22h32m00s;', 'exper_nominal_stop=2024y095d16h15m00s;']
		self.tracks['e24e07'] = ['exper_nominal_start=2024y098d00h59m00s;', 'exper_nominal_stop=2024y098d16h08m00s;']
		self.tracks['e24a08'] = ['exper_nominal_start=2024y098d18h31m00s;', 'exper_nominal_stop=2024y099d19h02m00s;']
		self.tracks['e24c09'] = ['exper_nominal_start=2024y099d22h12m00s;', 'exper_nominal_stop=2024y100d15h28m00s;']
		self.tracks['e24d10'] = ['exper_nominal_start=2024y100d22h59m00s;', 'exper_nominal_stop=2024y101d10h42m00s;']
		self.tracks['e24g11'] = ['exper_nominal_start=2024y101d22h55m00s;', 'exper_nominal_stop=2024y102d08h52m00s;']
		#
		self.tracks['c241a'] = ['exper_nominal_start=2024y109d16h00m00s;', 'exper_nominal_stop=2024y110d15h54m51s;']
		self.tracks['c241b'] = ['exper_nominal_start=2024y110d16h15m01s;', 'exper_nominal_stop=2024y112d10h52m00s;']
		self.tracks['c241c'] = ['exper_nominal_start=2024y112d00h40m00s;', 'exper_nominal_stop=2024y113d07h53m20s;']
		self.tracks['c241d'] = ['exper_nominal_start=2024y112d22h00m00s;', 'exper_nominal_stop=2024y114d16h56m31s;']
		#
		self.tracks['e23a22'] = ['exper_nominal_start=2023y111d15h18m00s;', 'exper_nominal_stop=2023y112d07h48m00s;']
		self.tracks['e23e19'] = ['exper_nominal_start=2023y109d04h34m00s;', 'exper_nominal_stop=2023y109d19h41m00s;']
		self.tracks['e23c18'] = ['exper_nominal_start=2023y108d02h21m00s;', 'exper_nominal_stop=2023y108d15h20m00s;']
		self.tracks['e23g17'] = ['exper_nominal_start=2023y107d03h06m00s;', 'exper_nominal_stop=2023y107d16h42m00s;']
		self.tracks['e23c16'] = ['exper_nominal_start=2023y106d02h29m00s;', 'exper_nominal_stop=2023y106d15h28m00s;']
		self.tracks['e23d15'] = ['exper_nominal_start=2023y105d01h43m00s;', 'exper_nominal_stop=2023y105d15h13m00s;']
		#
		self.tracks['e22f27'] = ['exper_nominal_start=2022y085d21h21m00s;', 'exper_nominal_stop=2022y086d12h21m00s;']
		self.tracks['e22a26'] = ['exper_nominal_start=2022y084d21h34m00s;', 'exper_nominal_stop=2022y085d11h41m00s;']
		self.tracks['e22d23'] = ['exper_nominal_start=2022y082d02h36m00s;', 'exper_nominal_stop=2022y082d16h39m00s;']
		self.tracks['e22e22'] = ['exper_nominal_start=2022y080d21h28m00s;', 'exper_nominal_stop=2022y081d16h00m30s;']
		self.tracks['e22c20'] = ['exper_nominal_start=2022y079d05h35m00s;', 'exper_nominal_stop=2022y079d21h38m00s;']
		self.tracks['e22b19'] = ['exper_nominal_start=2022y078d03h14m00s;', 'exper_nominal_stop=2022y078d19h18m00s;']
		self.tracks['e22g18'] = ['exper_nominal_start=2022y076d21h44m00s;', 'exper_nominal_stop=2022y077d12h45m00s;']
		#
		self.tracks['e22j25'] = ['exper_nominal_start=2022y025d04h10m00s;', 'exper_nominal_stop=2022y025d06h55m00s;']
		self.tracks['e22j26'] = ['exper_nominal_start=2022y026d04h06m00s;', 'exper_nominal_stop=2022y026d06h51m00s;']
		#
		self.tracks['e21b09'] = ['exper_nominal_start=2021y098d23h52m00s;', 'exper_nominal_stop=2021y099d15h23m00s;']
		self.tracks['e21e13'] = ['exper_nominal_start=2021y102d19h40m00s;', 'exper_nominal_stop=2021y103d11h40m00s;']
		self.tracks['e21a14'] = ['exper_nominal_start=2021y103d23h40m00s;', 'exper_nominal_stop=2021y104d15h50m00s;']
		self.tracks['e21d15'] = ['exper_nominal_start=2021y104d23h29m00s;', 'exper_nominal_stop=2021y105d15h42m00s;']
		self.tracks['e21a16'] = ['exper_nominal_start=2021y105d23h32m00s;', 'exper_nominal_stop=2021y106d15h02m00s;']
		self.tracks['e21a17'] = ['exper_nominal_start=2021y106d23h28m00s;', 'exper_nominal_stop=2021y107d15h38m00s;']
		self.tracks['e21e18'] = ['exper_nominal_start=2021y107d19h20m00s;', 'exper_nominal_stop=2021y108d11h49m00s;']
		self.tracks['e21f19'] = ['exper_nominal_start=2021y109d01h13m00s;', 'exper_nominal_stop=2021y109d06h08m00s;']
		#
		self.tracks['e18c21'] = ['exper_nominal_start=2018y110d22h38m00s;', 'exper_nominal_stop=2018y111d14h36m00s;']
		self.tracks['e18e22'] = ['exper_nominal_start=2018y111d22h31m00s;', 'exper_nominal_stop=2018y112d14h36m00s;']
		self.tracks['e18a24'] = ['exper_nominal_start=2018y114d03h02m00s;', 'exper_nominal_stop=2018y114d15h45m00s;']
		self.tracks['e18c25'] = ['exper_nominal_start=2018y114d22h22m00s;', 'exper_nominal_stop=2018y115d14h20m00s;']
		self.tracks['e18g27'] = ['exper_nominal_start=2018y116d19h30m00s;', 'exper_nominal_stop=2018y117d09h33m00s;']
		self.tracks['e18d28'] = ['exper_nominal_start=2018y117d21h57m00s;', 'exper_nominal_stop=2018y118d09h39m00s;']
		#
		self.tracks['e17d05'] = ['exper_nominal_start=2017y094d22h31m00s;', 'exper_nominal_stop=2017y095d17h07m00s;']
		self.tracks['e17b06'] = ['exper_nominal_start=2017y096d00h46m00s;', 'exper_nominal_stop=2017y096d16h14m00s;']
		self.tracks['e17c07'] = ['exper_nominal_start=2017y097d04h01m00s;', 'exper_nominal_stop=2017y097d20h42m00s;']
		self.tracks['e17a10'] = ['exper_nominal_start=2017y099d23h17m00s;', 'exper_nominal_stop=2017y100d15h10m00s;']
		self.tracks['e17e11'] = ['exper_nominal_start=2017y100d22h16m00s;', 'exper_nominal_stop=2017y101d15h22m00s;']


	def listTracks(self, year: int = -1) -> List[str]:

		tracklist = []

		if year==2025 or year<=0:
			tracklist += ['e25j21', 'e25c04', 'e25a06', 'e25f08']
		if year==2024 or year<=0:
			tracklist += ['e24j25', 'e24b04', 'e24e07', 'e24a08', 'e24c09', 'e24d10', 'e24g11']
			tracklist += ['c241a', 'c241b', 'c241c', 'c241d']
		if year==2023 or year<=0:
			tracklist += ['e23a22', 'e23c16', 'e23c18', 'e23d15', 'e23e19', 'e23g17']
		if year==2022 or year<=0:
			tracklist += ['e22j25', 'e22j26', 'e22g18', 'e22b19', 'e22c20', 'e22e22', 'e22d23', 'e22a26', 'e22f27', 'e22xxx']
		if year==2021 or year<=0:
			tracklist += ['e21b09', 'e21e13', 'e21a14', 'e21d15', 'e21a16', 'e21a17', 'e21e18', 'e21f19']
		if year==2018 or year<=0:
			tracklist += ['e18c21', 'e18e22', 'e18a24', 'e18c25', 'e18g27', 'e18d28']
		if year==2017 or year <=0:
			tracklist += ['e17d05', 'e17b06', 'e17c07', 'e17a10', 'e17e11']

		return tracklist


	def getTrackTimerange(self, trackname: str):

		if trackname not in self.tracks.keys():
			return None

		t0, t1 = self.tracks[trackname]
		gmt0 = self.getGMTimeFromVEXTime(t0)
		gmt1 = self.getGMTimeFromVEXTime(t1)
		timebracket = [gmt0, gmt1]

		return timebracket


	def getGMTimeFromVEXTime(self, t: str):

		t = t.split('=')[1]
		year, doy, hour, mins = int(t[0:4]), int(t[5:8]), int(t[9:11]), int(t[12:14])
		tt = datetime.datetime(year, 1, 1) + datetime.timedelta(days=doy-1) + datetime.timedelta(seconds=60*(60*hour + mins))
		gmt = calendar.timegm(tt.timetuple())

		return gmt
