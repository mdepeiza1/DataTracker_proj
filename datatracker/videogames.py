from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
from .models.videogames import VideoGames
from .models.videogames import videogames

bp = Blueprint('videogames', __name__)


@bp.route('/Investment', methods=['GET'])
def Investment():
    #videogames = VideoGames.objects.all()
    xlabels = []
    ylabels = []
    for videogame in videogames:
        xlabels.append(videogame.platform)
        ylabels.append(videogame.globalSales)
    return render_template('videogames/Investment.html', xs=xlabels, ys=ylabels)
