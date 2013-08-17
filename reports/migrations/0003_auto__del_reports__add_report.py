# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Reports'
        db.delete_table(u'reports_reports')

        # Removing M2M table for field copies on 'Reports'
        db.delete_table(db.shorten_name(u'reports_reports_copies'))

        # Adding model 'Report'
        db.create_table(u'reports_report', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('addressed_to', self.gf('django.db.models.fields.TextField')()),
            ('reported_from', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Member'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 8, 17, 0, 0))),
        ))
        db.send_create_signal(u'reports', ['Report'])

        # Adding M2M table for field copies on 'Report'
        m2m_table_name = db.shorten_name(u'reports_report_copies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('report', models.ForeignKey(orm[u'reports.report'], null=False)),
            ('topic', models.ForeignKey(orm[u'protocols.topic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['report_id', 'topic_id'])


    def backwards(self, orm):
        # Adding model 'Reports'
        db.create_table(u'reports_reports', (
            ('created_at', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 8, 17, 0, 0))),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('reported_from', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Member'])),
            ('addressed_to', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'reports', ['Reports'])

        # Adding M2M table for field copies on 'Reports'
        m2m_table_name = db.shorten_name(u'reports_reports_copies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('reports', models.ForeignKey(orm[u'reports.reports'], null=False)),
            ('topic', models.ForeignKey(orm[u'protocols.topic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['reports_id', 'topic_id'])

        # Deleting model 'Report'
        db.delete_table(u'reports_report')

        # Removing M2M table for field copies on 'Report'
        db.delete_table(db.shorten_name(u'reports_report_copies'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'members.member': {
            'Meta': {'object_name': 'Member'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'faculty_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '8'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'protocols.topic': {
            'Meta': {'object_name': 'Topic'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'reports.report': {
            'Meta': {'object_name': 'Report'},
            'addressed_to': ('django.db.models.fields.TextField', [], {}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'copies': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['protocols.Topic']", 'symmetrical': 'False'}),
            'created_at': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 8, 17, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reported_from': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['members.Member']"})
        }
    }

    complete_apps = ['reports']