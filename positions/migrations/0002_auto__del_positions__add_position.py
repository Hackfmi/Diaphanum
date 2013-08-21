# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Positions'
        db.delete_table(u'positions_positions')

        # Adding model 'Position'
        db.create_table(u'positions_position', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 8, 21, 0, 0))),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'positions', ['Position'])


    def backwards(self, orm):
        # Adding model 'Positions'
        db.create_table(u'positions_positions', (
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 8, 21, 0, 0))),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'positions', ['Positions'])

        # Deleting model 'Position'
        db.delete_table(u'positions_position')


    models = {
        u'positions.position': {
            'Meta': {'object_name': 'Position'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 8, 21, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['positions']