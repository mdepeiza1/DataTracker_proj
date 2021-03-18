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
    cutOffYear = int(2013);
    for videogame in videogames:
        if videogame.year is not None:
            if videogame.year >= cutOffYear:
                if videogame.platform in xlabels:
                    indexOfPlatform = xlabels.index(videogame.platform)
                    ylabels[indexOfPlatform] += videogame.globalSales
                else:
                    xlabels.append(videogame.platform)
                    ylabels.append(videogame.globalSales)
    xs = html.unescape(xlabels)
    ys = html.unescape(ylabels)
    return render_template('videogames/Investment.html', xs=xs, ys=ys)


@bp.route('/PublisherPerConsole', methods=['GET'])
def PublisherPerConsole():
    #videogames = VideoGames.objects.all()
    xlabels = []
    ylabels = []
    for videogame in videogames:
        if videogame.publisher + " " + videogame.platform in xlabels:
            indexOfPublisherAndPlatform = xlabels.index(videogame.publisher + " " + videogame.platform)
            ylabels[indexOfPublisherAndPlatform] += videogame.globalSales
        else:
            xlabels.append(videogame.publisher + " " + videogame.platform)
            ylabels.append(videogame.globalSales)
    xs = html.unescape(xlabels)
    ys = html.unescape(ylabels)
    return render_template('videogames/PublisherPerConsole.html', xs=xs, ys=ys)



@bp.route('/Search',methods=['GET','POST'])
def SearchName():
    if request.method == 'POST':
        game_title=request.form['title']
        error = None
        xlabels = []
        ylabels = []
        games = []
        if not game_title:
            error = 'You must enter a name'
        if error is not None:
            flash(error)
        else:
            for videogame in videogames:
                if videogame.name == game_title:
                    games.append(videogame)
                    if videogame.platform in xlabels:
                        indexOfPlatform = xlabels.index(videogame.platform)
                        ylabels[indexOfPlatform] += videogame.globalSales
                    else:
                        xlabels.append(videogame.platform)
                        ylabels.append(videogame.globalSales)

            xs = html.unescape(xlabels)
            ys = html.unescape(ylabels)
            return render_template('videogames/SearchResults.html', page_title=game_title, xs=xs, ys=ys,
                                           video_game=videogame, games=games)
    else:
        return render_template('videogames/Search.html')

@bp.route('/Evaluation', methods=['GET'])
def Evaluation():
    #videogames = VideoGames.objects.all()
    xlabels = []
    ylabels = []
    for videogame in videogames:
        if videogame.genre + " NA Sales" in xlabels:
            indexOfGenreAndnaSales = xlabels.index(videogame.genre + " NA Sales")
            ylabels[indexOfGenreAndnaSales] += videogame.naSales
        elif videogame.genre + " EU Sales" in xlabels:
            indexOfGenreAndeuSales = xlabels.index(videogame.genre + " EU Sales")
            ylabels[indexOfGenreAndeuSales] += videogame.euSales
        elif videogame.genre + " JP Sales" in xlabels:
            indexOfGenreAndjpSales = xlabels.index(videogame.genre + " JP Sales")
            ylabels[indexOfGenreAndjpSales] += videogame.jpSales
        elif videogame.genre + " Other Sales" in xlabels:
            indexOfGenreAndotherSales = xlabels.index(videogame.genre + " Other Sales")
            ylabels[indexOfGenreAndotherSales] += videogame.otherSales
        else:
            xlabels.append(videogame.genre + " NA Sales")
            xlabels.append(videogame.genre + " EU Sales")
            xlabels.append(videogame.genre + " JP Sales")
            xlabels.append(videogame.genre + " Other Sales")
            ylabels.append(videogame.naSales)
            ylabels.append(videogame.euSales)
            ylabels.append(videogame.jpSales)
            ylabels.append(videogame.otherSales)
    xs = html.unescape(xlabels)
    ys = html.unescape(ylabels)
    return render_template('videogames/Evaluation.html', xs=xs, ys=ys)

@bp.route('/Index')
def Index0():
    return render_template('videogames/Index.html')

@bp.route('/')
def Index1():
    return render_template('videogames/Index.html')
