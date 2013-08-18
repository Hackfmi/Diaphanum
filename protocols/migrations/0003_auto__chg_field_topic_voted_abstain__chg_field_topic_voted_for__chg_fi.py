# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Topic.voted_abstain'
        db.alter_column(u'protocols_topic', 'voted_abstain', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'Topic.voted_for'
        db.alter_column(u'protocols_topic', 'voted_for', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'Topic.voted_against'
        db.alter_column(u'protocols_topic', 'voted_against', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'Topic.statement'
        db.alter_column(u'protocols_topic', 'statement', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'Topic.voted_abstain'
        db.alter_column(u'protocols_topic', 'voted_abstain', self.gf('django.db.models.fields.PositiveIntegerField')(default=0))

        # Changing field 'Topic.voted_for'
        db.alter_column(u'protocols_topic', 'voted_for', self.gf('django.db.models.fields.PositiveIntegerField')(default=0))

        # Changing field 'Topic.voted_against'
        db.alter_column(u'protocols_topic', 'voted_against', self.gf('django.db.models.fields.PositiveIntegerField')(default=0))

        # Changing field 'Topic.statement'
        db.alter_column(u'protocols_topic', 'statement', self.gf('django.db.models.fields.TextField')(default=0))

    models = {
        u'attachments.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'file_name': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
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
        u'members.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'faculty_number': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
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
        u'protocols.institution': {
            'Meta': {'object_name': 'Institution'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'protocols.protocol': {
            'Meta': {'object_name': 'Protocol'},
            'absent': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'meetings_absent'", 'symmetrical': 'False', 'to': u"orm['members.User']"}),
            'additional': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'attendents': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'meetings_attend'", 'symmetrical': 'False', 'to': u"orm['members.User']"}),
            'conducted_at': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'current_majority': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'information': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['protocols.Institution']"}),
            'majority': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'quorum': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'scheduled_time': ('django.db.models.fields.TimeField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'topics': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['protocols.Topic']", 'symmetrical': 'False'})
        },
        u'protocols.topic': {
            'Meta': {'object_name': 'Topic'},
            'attachment': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['attachments.Attachment']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'statement': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'voted_abstain': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voted_against': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voted_for': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['protocols']