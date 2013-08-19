# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Topic'
        db.create_table(u'protocols_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'protocols', ['Topic'])

        # Adding M2M table for field attachment on 'Topic'
        m2m_table_name = db.shorten_name(u'protocols_topic_attachment')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('topic', models.ForeignKey(orm[u'protocols.topic'], null=False)),
            ('attachment', models.ForeignKey(orm[u'attachments.attachment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['topic_id', 'attachment_id'])

        # Adding model 'Protocol'
        db.create_table(u'protocols_protocol', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('scheduled_time', self.gf('django.db.models.fields.TimeField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('quorum', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('absent', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('voted_for', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('voted_against', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('voted_abstain', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('information', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'protocols', ['Protocol'])

        # Adding M2M table for field attendents on 'Protocol'
        m2m_table_name = db.shorten_name(u'protocols_protocol_attendents')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('protocol', models.ForeignKey(orm[u'protocols.protocol'], null=False)),
            ('user', models.ForeignKey(orm[u'members.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['protocol_id', 'user_id'])

        # Adding M2M table for field topics on 'Protocol'
        m2m_table_name = db.shorten_name(u'protocols_protocol_topics')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('protocol', models.ForeignKey(orm[u'protocols.protocol'], null=False)),
            ('topic', models.ForeignKey(orm[u'protocols.topic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['protocol_id', 'topic_id'])

        # Adding M2M table for field attachments on 'Protocol'
        m2m_table_name = db.shorten_name(u'protocols_protocol_attachments')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('protocol', models.ForeignKey(orm[u'protocols.protocol'], null=False)),
            ('attachment', models.ForeignKey(orm[u'attachments.attachment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['protocol_id', 'attachment_id'])


    def backwards(self, orm):
        # Deleting model 'Topic'
        db.delete_table(u'protocols_topic')

        # Removing M2M table for field attachment on 'Topic'
        db.delete_table(db.shorten_name(u'protocols_topic_attachment'))

        # Deleting model 'Protocol'
        db.delete_table(u'protocols_protocol')

        # Removing M2M table for field attendents on 'Protocol'
        db.delete_table(db.shorten_name(u'protocols_protocol_attendents'))

        # Removing M2M table for field topics on 'Protocol'
        db.delete_table(db.shorten_name(u'protocols_protocol_topics'))

        # Removing M2M table for field attachments on 'Protocol'
        db.delete_table(db.shorten_name(u'protocols_protocol_attachments'))


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
        u'protocols.protocol': {
            'Meta': {'object_name': 'Protocol'},
            'absent': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'attachments': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['attachments.Attachment']", 'symmetrical': 'False'}),
            'attendents': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'protocols'", 'symmetrical': 'False', 'to': u"orm['members.User']"}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'information': ('django.db.models.fields.TextField', [], {}),
            'number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'quorum': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'scheduled_time': ('django.db.models.fields.TimeField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'topics': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['protocols.Topic']", 'symmetrical': 'False'}),
            'voted_abstain': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'voted_against': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'voted_for': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'protocols.topic': {
            'Meta': {'object_name': 'Topic'},
            'attachment': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['attachments.Attachment']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['protocols']