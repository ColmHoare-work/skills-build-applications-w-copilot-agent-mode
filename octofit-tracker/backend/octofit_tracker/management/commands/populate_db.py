from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        octo_models.Team.objects.all().delete()
        octo_models.Activity.objects.all().delete()
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Workout.objects.all().delete()

        # Create Teams
        marvel = octo_models.Team.objects.create(name='Marvel')
        dc = octo_models.Team.objects.create(name='DC')

        # Create Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        captain = User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Create Activities
        octo_models.Activity.objects.create(user=ironman, type='run', duration=30, distance=5)
        octo_models.Activity.objects.create(user=batman, type='cycle', duration=60, distance=20)
        octo_models.Activity.objects.create(user=superman, type='swim', duration=45, distance=2)
        octo_models.Activity.objects.create(user=captain, type='run', duration=25, distance=4)

        # Create Workouts
        octo_models.Workout.objects.create(name='Hero HIIT', description='High intensity workout for heroes')
        octo_models.Workout.objects.create(name='Power Lift', description='Strength training for super strength')

        # Create Leaderboard
        octo_models.Leaderboard.objects.create(user=ironman, points=100)
        octo_models.Leaderboard.objects.create(user=batman, points=90)
        octo_models.Leaderboard.objects.create(user=superman, points=95)
        octo_models.Leaderboard.objects.create(user=captain, points=85)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
