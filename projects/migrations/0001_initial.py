# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'projects_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('flp', self.gf('django.db.models.fields.related.ForeignKey')(related_name='flp', to=orm['members.User'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('targets', self.gf('django.db.models.fields.TextField')()),
            ('tasks', self.gf('django.db.models.fields.TextField')()),
            ('target_group', self.gf('django.db.models.fields.TextField')()),
            ('schedule', self.gf('django.db.models.fields.TextField')()),
            ('resources', self.gf('django.db.models.fields.TextField')()),
            ('finance_description', self.gf('django.db.models.fields.TextField')()),
            ('partners', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'projects', ['Project'])

        # Adding M2M table for field team on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_team')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('user', models.ForeignKey(orm[u'members.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'user_id'])

        # Adding M2M table for field files on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_files')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('attachment', models.ForeignKey(orm[u'attachments.attachment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'attachment_id'])

    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'projects_project')

        # Removing M2M table for field team on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_team'))

        # Removing M2M table for field files on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_files'))


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
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['attachments.Attachment']", 'symmetrical': 'False'}),
            'finance_description': ('django.db.models.fields.TextField', [], {}),
            'flp': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'flp'", 'to': u"orm['members.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'partners': ('django.db.models.fields.TextField', [], {}),
            'resources': ('django.db.models.fields.TextField', [], {}),
            'schedule': ('django.db.models.fields.TextField', [], {}),
            'target_group': ('django.db.models.fields.TextField', [], {}),
            'targets': ('django.db.models.fields.TextField', [], {}),
            'tasks': ('django.db.models.fields.TextField', [], {}),
            'team': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'team'", 'symmetrical': 'False', 'to': u"orm['members.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['members.User']"})
        }
    }

    complete_apps = ['projects']
