{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import math\n",
    "from flask import Flask, jsonify, request\n",
    "from folium import plugins\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "@app.route('/search/<latitude>/<longitude>', methods=['GET'])\n",
    "def search(latitude,longitude):\n",
    "    df = pd.read_csv('./CSV_part4.csv', sep=',')\n",
    "    source =(float(latitude),float(longitude))\n",
    "    df['distance']= df.apply(lambda x: distance(source,(x['latitude'],x['longitude'])), axis=1)\n",
    "    results=df.sort_values(by='distance', ascending=True).head(10)\n",
    "    out = results.to_dict(orient='records')\n",
    "    return jsonify({'results': out})\n",
    "\n",
    "@app.route('/test', methods = ['GET'])\n",
    "def getTest():\n",
    "    return jsonify({'parcelid' : 1})\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "@app.errorhandler(404)\n",
    "def not_found(error):\n",
    "    return make_response(jsonify({'error': 'Not found'}), 404)\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    return \"Hello, World!\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "if __name__ == '__main__':\n",
    "    app.run(debug= True, port = 5000, host ='0.0.0.0')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [conda root]",
   "language": "python",
   "name": "conda-root-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
