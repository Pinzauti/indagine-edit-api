from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Data
from .serializers import DataSerializer
from django.db.models import Sum


def percentage(number, total):
	return round(100*number/total,0)


class DataView(viewsets.ModelViewSet):
	queryset = Data.objects.all()[:2000]  # a causa del piano free di heroku, limite eliminabile in locale
	serializer_class = DataSerializer
	http_method_names = ['get']


class GenderView(APIView):
	def get(self, request):
		male = Data.objects.filter(GENERE="Maschio").count()
		female = Data.objects.filter(GENERE="Femmina").count()
		maleAccidents = Data.objects.filter(ALMENO_1_INCIDENTE="Si", GENERE="Maschio").count()
		femaleAccidents = Data.objects.filter(ALMENO_1_INCIDENTE="Si", GENERE="Femmina").count()
		content = {'name': 'Maschi', 'value': percentage(maleAccidents, male)}, {'name': 'Femmine', 'value': percentage(femaleAccidents, female)}
		return Response(content)


class AlcoholView(APIView):
	def get(self, request):
		drunkAccidents = Data.objects.filter(GUIDA_UBRIACO="Si", ALMENO_1_INCIDENTE="Si").count()
		drunk = Data.objects.filter(GUIDA_UBRIACO="Si", ALMENO_1_INCIDENTE="No").count()
		notDrunkAccidents = Data.objects.filter(GUIDA_UBRIACO="No", ALMENO_1_INCIDENTE="Si").count()
		notDrunk = Data.objects.filter(GUIDA_UBRIACO="No", ALMENO_1_INCIDENTE="No").count()
		content = {'name': 'Guidato ubriaco', 'Hanno avuto incidenti': drunkAccidents,
		           'Mai avuto incidenti': drunk}, {'name': 'Mai fatto',
		                                           'Hanno avuto incidenti': notDrunkAccidents,
		                                           'Mai avuto incidenti': notDrunk}
		return Response(content)


class DrugsView(APIView):
	def get(self, request):
		dopedAccidents = Data.objects.filter(GUIDA_DOPO_DROGA="Si", ALMENO_1_INCIDENTE="Si").count()
		doped = Data.objects.filter(GUIDA_DOPO_DROGA="Si", ALMENO_1_INCIDENTE="No").count()
		notDopedAccidents = Data.objects.filter(GUIDA_DOPO_DROGA="No", ALMENO_1_INCIDENTE="Si").count()
		notDoped = Data.objects.filter(GUIDA_DOPO_DROGA="No", ALMENO_1_INCIDENTE="No").count()
		content = {'name': 'Guidato drogato', 'Hanno avuto incidenti': dopedAccidents,
		           'Mai avuto incidenti': doped}, {'name': 'Mai fatto',
		                                           'Hanno avuto incidenti': notDopedAccidents,
		                                           'Mai avuto incidenti': notDoped}
		return Response(content)


class LifeStyleView(APIView):
	def get(self, request):
		sport = Data.objects.filter(ALMENO_1_INCIDENTE="No", ATTIVITA_FISICA="Non faccio mai attività fisica").count()
		bullied = Data.objects.filter(ALMENO_1_INCIDENTE="No", SUBITO_PREPOTENZE="Si").count()
		condom = Data.objects.filter(ALMENO_1_INCIDENTE="No", USO_PRESERVATIVO="No").count()
		vegetables = Data.objects.filter(ALMENO_1_INCIDENTE="No", CONSUMO_VERDURA="Raramente o mai").count()
		fruit = Data.objects.filter(ALMENO_1_INCIDENTE="No", CONSUMO_FRUTTA="Raramente o mai").count()
		drugs = Data.objects.filter(ALMENO_1_INCIDENTE="No", SOSTANZE_VITA="Si").count()
		noAccidents = Data.objects.filter(ALMENO_1_INCIDENTE="No").count()
		content = {'name': 'No sport', 'n': percentage(sport, noAccidents),'fill': '#8884d8'}, {'name': 'Subito bullismo', 'n': percentage(bullied,noAccidents),
		                                                                'fill': '#83a6ed'}, \
		          {'name': 'No uso preservativo', 'n': percentage(condom, noAccidents),'fill': '#8dd1e1'}, {'name': 'No verdure',
		                                                                            'n': percentage(vegetables, noAccidents),'fill': '#82ca9d'}, \
		          {'name': 'No frutta', 'n': percentage(fruit,noAccidents), 'fill': '#a4de6c'}, {'name': 'Uso droghe', 'n': percentage(drugs,noAccidents),
		                                                                 'fill': '#d0ed57'}, \
		          {'name': 'Nessun incidente', 'n': "100", 'fill': '#ffc658'},
		return Response(content)


class AccidentsLifeStyleView(APIView):
	def get(self, request):
		sport = Data.objects.filter(ALMENO_1_INCIDENTE="Si", ATTIVITA_FISICA="Non faccio mai attività fisica").count()
		bullied = Data.objects.filter(ALMENO_1_INCIDENTE="Si", SUBITO_PREPOTENZE="Si").count()
		condom = Data.objects.filter(ALMENO_1_INCIDENTE="Si", USO_PRESERVATIVO="No").count()
		vegetables = Data.objects.filter(ALMENO_1_INCIDENTE="Si", CONSUMO_VERDURA="Raramente o mai").count()
		fruit = Data.objects.filter(ALMENO_1_INCIDENTE="Si", CONSUMO_FRUTTA="Raramente o mai").count()
		drugs = Data.objects.filter(ALMENO_1_INCIDENTE="Si", SOSTANZE_VITA="Si").count()
		Accidents = Data.objects.filter(ALMENO_1_INCIDENTE="Si").count()
		content = {'name': 'No sport', 'n': percentage(sport, Accidents), 'fill': '#8884d8'}, {'name': 'Subito bullismo', 'n': percentage(bullied,Accidents),
		                                                                'fill': '#83a6ed'}, \
		          {'name': 'No uso preservativo', 'n': percentage(condom, Accidents),'fill': '#8dd1e1'}, {'name': 'No verdure',
		                                                                            'n': percentage(vegetables,Accidents), 'fill': '#82ca9d'}, \
		          {'name': 'No frutta', 'n': percentage(fruit,Accidents), 'fill': '#a4de6c'}, {'name': 'Uso droghe', 'n': percentage(drugs,Accidents),
		                                                                 'fill': '#d0ed57'}, \
		          {'name': 'Coinvolti in incidenti', 'n': "100", 'fill': '#ffc658'},
		return Response(content)


class DrunkView(APIView):
	def get(self, request):
		zeroAccident = Data.objects.filter(ALMENO_1_INCIDENTE="No").count()
		zeroAccidentDrunk = Data.objects.filter(ALMENO_1_INCIDENTE="No").aggregate(
			Sum('FREQUENZA_UBRIACATO_ANNO'))
		zeroAccidentAverage = zeroAccidentDrunk['FREQUENZA_UBRIACATO_ANNO__sum'] / zeroAccident

		oneAccident = Data.objects.filter(ALMENO_1_INCIDENTE="Si", NUM_INCIDENTI=1).count()
		oneAccidentDrunk = Data.objects.filter(ALMENO_1_INCIDENTE="Si", NUM_INCIDENTI=1).aggregate(
			Sum('FREQUENZA_UBRIACATO_ANNO'))
		oneAccidentAverage = oneAccidentDrunk['FREQUENZA_UBRIACATO_ANNO__sum'] / oneAccident

		twoAccident = Data.objects.filter(ALMENO_1_INCIDENTE="Si", NUM_INCIDENTI=2).count()
		twoAccidentDrunk = Data.objects.filter(ALMENO_1_INCIDENTE="Si", NUM_INCIDENTI=2).aggregate(
			Sum('FREQUENZA_UBRIACATO_ANNO'))
		twoAccidentAverage = twoAccidentDrunk['FREQUENZA_UBRIACATO_ANNO__sum'] / twoAccident

		threeAccident = Data.objects.filter(ALMENO_1_INCIDENTE="Si", NUM_INCIDENTI=3).count()
		threeAccidentDrunk = Data.objects.filter(ALMENO_1_INCIDENTE="Si", NUM_INCIDENTI=3).aggregate(
			Sum('FREQUENZA_UBRIACATO_ANNO'))
		threeAccidentAverage = threeAccidentDrunk['FREQUENZA_UBRIACATO_ANNO__sum'] / threeAccident

		fourAccident = Data.objects.filter(ALMENO_1_INCIDENTE="Si", NUM_INCIDENTI=4).count()
		fourAccidentDrunk = Data.objects.filter(ALMENO_1_INCIDENTE="Si", NUM_INCIDENTI=4).aggregate(
			Sum('FREQUENZA_UBRIACATO_ANNO'))
		fourAccidentAverage = fourAccidentDrunk['FREQUENZA_UBRIACATO_ANNO__sum'] / fourAccident
		
		content = {"Numero di incidenti": 0, "Ubriacature nell'ultimo anno": round(zeroAccidentAverage, 0)}, {
			"Numero di incidenti": 1, "Ubriacature nell'ultimo anno": round(oneAccidentAverage, 0)}, {
			          "Numero di incidenti": 2, "Ubriacature nell'ultimo anno": round(twoAccidentAverage, 0)}, \
		          {"Numero di incidenti": 3, "Ubriacature nell'ultimo anno": round(threeAccidentAverage, 0)}, {
			          "Numero di incidenti": 4, "Ubriacature nell'ultimo anno": round(fourAccidentAverage, 0)},
		return Response(content)


class SmokeView(APIView):
	def get(self, request):
		smokeAccidents = Data.objects.filter(ATTUALMENTE_FUMI="Si", ALMENO_1_INCIDENTE="Si").count()
		smoke = Data.objects.filter(ATTUALMENTE_FUMI="Si", ALMENO_1_INCIDENTE="No").count()
		notSmokeAccidents = Data.objects.filter(ATTUALMENTE_FUMI="No", ALMENO_1_INCIDENTE="Si").count()
		notSmoke = Data.objects.filter(ATTUALMENTE_FUMI="No", ALMENO_1_INCIDENTE="No").count()
		content = {'name': 'Fumatori', 'Hanno avuto incidenti': smokeAccidents,
		           'Mai avuto incidenti': smoke}, {'name': 'Non fumatori', 'Hanno avuto incidenti': notSmokeAccidents,
		                                           'Mai avuto incidenti': notSmoke}
		return Response(content)


class DroveWithDrunkView(APIView):
	def get(self, request):
		withDrunkAccidents = Data.objects.filter(SU_MEZZO_CON_UBRIACO="Si", ALMENO_1_INCIDENTE="Si").count()
		withDrunk = Data.objects.filter(SU_MEZZO_CON_UBRIACO="Si", ALMENO_1_INCIDENTE="No").count()
		notWithDrunkAccidents = Data.objects.filter(SU_MEZZO_CON_UBRIACO="No", ALMENO_1_INCIDENTE="Si").count()
		notWithDrunk = Data.objects.filter(SU_MEZZO_CON_UBRIACO="No", ALMENO_1_INCIDENTE="No").count()
		content = {'name': 'Su mezzo con ubriaco', 'Hanno avuto incidenti': withDrunkAccidents,
		           'Mai avuto incidenti': withDrunk}, {'name': 'Mai fatto',
		                                               'Hanno avuto incidenti': notWithDrunkAccidents,
		                                               'Mai avuto incidenti': notWithDrunk}
		return Response(content)


class BMIView(APIView):
	def get(self, request):
		underweight1 = Data.objects.filter(BMI_6CLASSI="SOTTOPESO I").count()
		underweight1Accident = Data.objects.filter(ALMENO_1_INCIDENTE="Si", BMI_6CLASSI="SOTTOPESO I").count()

		underweight2 = Data.objects.filter(BMI_6CLASSI="SOTTOPESO II").count()
		underweight2Accident = Data.objects.filter(ALMENO_1_INCIDENTE="Si", BMI_6CLASSI="SOTTOPESO II").count()

		underweight3 = Data.objects.filter(BMI_6CLASSI="SOTTOPESO III").count()
		underweight3Accident = Data.objects.filter(ALMENO_1_INCIDENTE="Si", BMI_6CLASSI="SOTTOPESO III").count()

		normalweight = Data.objects.filter(BMI_6CLASSI="NORMOPESO").count()
		normalweightAccident = Data.objects.filter(ALMENO_1_INCIDENTE="Si", BMI_6CLASSI="NORMOPESO").count()

		overweight = Data.objects.filter(BMI_6CLASSI="SOVRAPPESO").count()
		overweightAccident = Data.objects.filter(ALMENO_1_INCIDENTE="Si", BMI_6CLASSI="SOVRAPPESO").count()

		obese = Data.objects.filter(BMI_6CLASSI="OBESO").count()
		obeseAccident = Data.objects.filter(ALMENO_1_INCIDENTE="Si", BMI_6CLASSI="OBESO").count()

		content = {'name': "Sottopeso I", "Percentuale incidenti": percentage(underweight1Accident, underweight1)}, {'name': "Sottopeso II", "Percentuale incidenti": percentage(underweight2Accident, underweight2)}, \
		          {'name': "Sottopeso III", "Percentuale incidenti": percentage(underweight3Accident, underweight3)}, {'name': "Normopeso", "Percentuale incidenti": percentage(normalweightAccident, normalweight)}, \
		          {'name': "Sovrappeso", "Percentuale incidenti": percentage(overweightAccident, overweight)}, {'name': "Obeso", "Percentuale incidenti": percentage(obeseAccident, obese)},

		return Response(content)
