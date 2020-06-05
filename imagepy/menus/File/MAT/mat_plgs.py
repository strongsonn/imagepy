from imagepy.core.util import fileio
from scipy.io import savemat, loadmat
from sciapp import Source
import os

Source.manager('reader').add(name='mat', obj=lambda path: loadmat(path)['img'])
Source.manager('writer').add(name='mat', obj=lambda path, img: savemat(path, {'img':img}))

class OpenFile(fileio.Reader):
	title = 'Mat Open'
	filt = ['Mat']

class SaveFile(fileio.Writer):
	title = 'Mat Save'
	filt = ['mat']

class Open3D(fileio.Reader):
	title = 'Mat 3D Open'
	filt = ['Mat']

	def run(self, para = None):
		imgs = loadmat(para['path'])['img']
		fp, fn = os.path.split(para['path'])
		fn, fe = os.path.splitext(fn) 
		IPy.show_img(imgs, fn)

class Save3D(fileio.Writer):
	title = 'Mat 3D Save'
	filt = ['mat']
	note = ['8-bit', 'rgb', 'stack']

	def run(self, ips, imgs, para = None):
		savemat(para['path'], {'img':imgs})

plgs = [OpenFile, SaveFile, '-', Open3D, Save3D]