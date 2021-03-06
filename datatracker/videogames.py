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


@bp.route('/PublisherPerConsole', methods=['GET','POST'])
def PublisherPerConsole():
    if request.method == 'POST':
        platform = request.form['platform']
        #videogames = VideoGames.objects.all()
        x_labels = []
        y_labels = []
        for videogame in videogames:
            if videogame.platform == platform:
                if videogame.publisher in x_labels:
                    index_pub = x_labels.index(videogame.publisher)
                    y_labels[index_pub] += videogame.globalSales
                else:
                    x_labels.append(videogame.publisher)
                    y_labels.append(videogame.globalSales)

        xs = html.unescape(x_labels)
        ys = html.unescape(y_labels)
        return render_template('videogames/PublisherPerConsole.html', xs=xs, ys=ys)

    else:
        return render_template('videogames/PublisherPerConsole.html',xs = html.unescape([]), ys = html.unescape([]))


@bp.route('/Search',methods=['GET','POST'])
def SearchName():
    if request.method == 'POST':
        game_title = request.form['title']
        error = None
        xlabels = []
        ylabels = []
        games = []
        if not game_title:
            error = 'You must enter a name'
        for videogame in videogames:
            if game_title.upper() == videogame.name.upper():
                errorGameTitle = False
                break
            else:
                errorGameTitle = True
        if errorGameTitle == True:
            error = 'That game is not in the database'
        if error is not None:
            flash(error)
            return render_template('videogames/Search.html', error=error)
        else:
            for videogame in videogames:
                if videogame.name.upper() == game_title.upper():
                    videogame_title = videogame.name
                    games.append(videogame)
                    if videogame.platform in xlabels:
                        indexOfPlatform = xlabels.index(videogame.platform)
                        ylabels[indexOfPlatform] += videogame.globalSales
                    else:
                        xlabels.append(videogame.platform)
                        ylabels.append(videogame.globalSales)

            xs = html.unescape(xlabels)
            ys = html.unescape(ylabels)
            return render_template('videogames/SearchResults.html', page_title=videogame_title, xs=xs, ys=ys,
                                           video_game=games[0], games=games)
    else:
        return render_template('videogames/Search.html')


@bp.route('/Evaluation', methods=['GET','POST'])
def GenreByRegion():
    if request.method == 'POST':
        region = request.form['region']
        error = None
        #videogames = VideoGames.objects.all()
        xlabels = []
        ylabels = []

        if region == "global":
            for videogame in videogames:
                if videogame.genre + " Global Sales" in xlabels:
                    index_global = xlabels.index(videogame.genre + " Global Sales")
                    ylabels[index_global] += videogame.globalSales
                else:
                    xlabels.append(videogame.genre + " Global Sales")
                    ylabels.append(videogame.globalSales)
            xs = html.unescape(xlabels)
            ys = html.unescape(ylabels)
            return render_template('videogames/Evaluation.html', xs=xs, ys=ys, region="global")
        elif region == "na":
            for videogame in videogames:
                if videogame.genre + " North America Sales" in xlabels:
                    index_na = xlabels.index(videogame.genre + " North America Sales")
                    ylabels[index_na] += videogame.naSales
                else:
                    xlabels.append(videogame.genre + " North America Sales")
                    ylabels.append(videogame.naSales)
            xs = html.unescape(xlabels)
            ys = html.unescape(ylabels)
            return render_template('videogames/Evaluation.html', xs=xs, ys=ys, region="na")
        elif region == "eu":
            for videogame in videogames:
                if videogame.genre + " Europe Sales" in xlabels:
                    index_eu = xlabels.index(videogame.genre + " Europe Sales")
                    ylabels[index_eu] += videogame.euSales
                else:
                    xlabels.append(videogame.genre + " Europe Sales")
                    ylabels.append(videogame.euSales)
            xs = html.unescape(xlabels)
            ys = html.unescape(ylabels)
            return render_template('videogames/Evaluation.html', xs=xs, ys=ys, region="eu")
        elif region == "jp":
            for videogame in videogames:
                if videogame.genre + " Japan Sales" in xlabels:
                    index_jp = xlabels.index(videogame.genre + " Japan Sales")
                    ylabels[index_jp] += videogame.jpSales
                else:
                    xlabels.append(videogame.genre + " Japan Sales")
                    ylabels.append(videogame.jpSales)
            xs = html.unescape(xlabels)
            ys = html.unescape(ylabels)
            return render_template('videogames/Evaluation.html', xs=xs, ys=ys, region="jp")
        elif region == "other":
            for videogame in videogames:
                if videogame.genre + " Other Sales" in xlabels:
                    index_other = xlabels.index(videogame.genre + " Other Sales")
                    ylabels[index_other] += videogame.otherSales
                else:
                    xlabels.append(videogame.genre + " Other Sales")
                    ylabels.append(videogame.otherSales)
            xs = html.unescape(xlabels)
            ys = html.unescape(ylabels)
            return render_template('videogames/Evaluation.html', xs=xs, ys=ys, region="other")

    else:
        xlabels = []
        ylabels = []

        for videogame in videogames:
            if videogame.genre + " Global Sales" in xlabels:
                index_global = xlabels.index(videogame.genre + " Global Sales")
                ylabels[index_global] += videogame.globalSales
            else:
                xlabels.append(videogame.genre + " Global Sales")
                ylabels.append(videogame.globalSales)
        xs = html.unescape(xlabels)
        ys = html.unescape(ylabels)
        return render_template('videogames/Evaluation.html', xs=xs, ys=ys, region="global")


@bp.route('/Index')
def Index0():
    return render_template('videogames/index.html')

@bp.route('/')
def Index1():
    return render_template('videogames/index.html')

