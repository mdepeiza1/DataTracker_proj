from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
from .models.videogames import VideoGames

bp = Blueprint('videogames', __name__)


@bp.route('/Investment', methods=['GET'])
def Investment():
    #videogames = VideoGames.objects.all()
    return render_template('videogames/Investment.html')#, videogames=videogames)
