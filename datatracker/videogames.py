from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
from .models.videogames import VideoGames
from .models.videogames import videogames
import html

bp = Blueprint('videogames', __name__)


@bp.route('/Investment', methods=['GET'])
def Investment():
    #videogames = VideoGames.objects.all()
    xlabels = []
    ylabels = []
    for videogame in videogames:
        if videogame.platform in xlabels:
            indexOfPlatform = xlabels.index(videogame.platform)
            ylabels[indexOfPlatform] += videogame.globalSales
        else:
            xlabels.append(videogame.platform)
            ylabels.append(videogame.globalSales)
    xs = html.unescape(xlabels)
    ys = html.unescape(ylabels)
    return render_template('videogames/Investment.html', xs=xs, ys=ys)
