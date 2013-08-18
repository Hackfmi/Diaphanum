# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Project.flp'
        db.alter_column(u'projects_project', 'flp_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.User']))

        # Changing field 'Project.user'
        db.alter_column(u'projects_project', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.User']))

    def backwards(self, orm):

        # Changing field 'Project.flp'
        db.alter_column(u'projects_project', 'flp_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Member']))

        # Changing field 'Project.user'
        db.alter_column(u'projects_project', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Member']))

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
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['attachments.Attachment']", 'symmetrical': 'False'}),
            'finance_description': ('django.db.models.fields.TextField', [], {}),
            'flp': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'flp'", 'to': u"orm['members.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'partners': ('django.db.models.fields.TextField', [], {}),
            'resources': ('django.db.models.fields.TextField', [], {}),
            'schedule': ('django.db.models.fields.TextField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'unrevised'", 'max_length': '50'}),
            'target_group': ('django.db.models.fields.TextField', [], {}),
            'targets': ('django.db.models.fields.TextField', [], {}),
            'tasks': ('django.db.models.fields.TextField', [], {}),
            'team': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'team'", 'symmetrical': 'False', 'to': u"orm['members.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['members.User']"})
        }
    }

    complete_apps = ['projects']