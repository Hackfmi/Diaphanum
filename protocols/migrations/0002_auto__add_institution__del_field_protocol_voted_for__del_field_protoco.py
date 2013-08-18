# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Institution'
        db.create_table(u'protocols_institution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'protocols', ['Institution'])

        # Deleting field 'Protocol.voted_for'
        db.delete_column(u'protocols_protocol', 'voted_for')

        # Deleting field 'Protocol.voted_against'
        db.delete_column(u'protocols_protocol', 'voted_against')

        # Deleting field 'Protocol.date'
        db.delete_column(u'protocols_protocol', 'date')

        # Deleting field 'Protocol.absent'
        db.delete_column(u'protocols_protocol', 'absent')

        # Deleting field 'Protocol.voted_abstain'
        db.delete_column(u'protocols_protocol', 'voted_abstain')

        # Adding field 'Protocol.conducted_at'
        db.add_column(u'protocols_protocol', 'conducted_at',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Protocol.institution'
        db.add_column(u'protocols_protocol', 'institution',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['protocols.Institution']),
                      keep_default=False)

        # Adding field 'Protocol.additional'
        db.add_column(u'protocols_protocol', 'additional',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Protocol.majority'
        db.add_column(u'protocols_protocol', 'majority',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Protocol.current_majority'
        db.add_column(u'protocols_protocol', 'current_majority',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)

        # Removing M2M table for field attachments on 'Protocol'
        db.delete_table(db.shorten_name(u'protocols_protocol_attachments'))

        # Adding M2M table for field absent on 'Protocol'
        m2m_table_name = db.shorten_name(u'protocols_protocol_absent')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('protocol', models.ForeignKey(orm[u'protocols.protocol'], null=False)),
            ('user', models.ForeignKey(orm[u'members.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['protocol_id', 'user_id'])


        # Changing field 'Protocol.information'
        db.alter_column(u'protocols_protocol', 'information', self.gf('django.db.models.fields.TextField')(null=True))
        # Adding field 'Topic.voted_for'
        db.add_column(u'protocols_topic', 'voted_for',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Topic.voted_against'
        db.add_column(u'protocols_topic', 'voted_against',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Topic.voted_abstain'
        db.add_column(u'protocols_topic', 'voted_abstain',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Topic.statement'
        db.add_column(u'protocols_topic', 'statement',
                      self.gf('django.db.models.fields.TextField')(default=1),
                      keep_default=False)


        # Changing field 'Topic.description'
        db.alter_column(u'protocols_topic', 'description', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):
        # Deleting model 'Institution'
        db.delete_table(u'protocols_institution')

        # Adding field 'Protocol.voted_for'
        db.add_column(u'protocols_protocol', 'voted_for',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Protocol.voted_against'
        db.add_column(u'protocols_protocol', 'voted_against',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Protocol.date'
        db.add_column(u'protocols_protocol', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Protocol.absent'
        db.add_column(u'protocols_protocol', 'absent',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Protocol.voted_abstain'
        db.add_column(u'protocols_protocol', 'voted_abstain',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)

        # Deleting field 'Protocol.conducted_at'
        db.delete_column(u'protocols_protocol', 'conducted_at')

        # Deleting field 'Protocol.institution'
        db.delete_column(u'protocols_protocol', 'institution_id')

        # Deleting field 'Protocol.additional'
        db.delete_column(u'protocols_protocol', 'additional')

        # Deleting field 'Protocol.majority'
        db.delete_column(u'protocols_protocol', 'majority')

        # Deleting field 'Protocol.current_majority'
        db.delete_column(u'protocols_protocol', 'current_majority')

        # Adding M2M table for field attachments on 'Protocol'
        m2m_table_name = db.shorten_name(u'protocols_protocol_attachments')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('protocol', models.ForeignKey(orm[u'protocols.protocol'], null=False)),
            ('attachment', models.ForeignKey(orm[u'attachments.attachment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['protocol_id', 'attachment_id'])

        # Removing M2M table for field absent on 'Protocol'
        db.delete_table(db.shorten_name(u'protocols_protocol_absent'))


        # Changing field 'Protocol.information'
        db.alter_column(u'protocols_protocol', 'information', self.gf('django.db.models.fields.TextField')(default=1))
        # Deleting field 'Topic.voted_for'
        db.delete_column(u'protocols_topic', 'voted_for')

        # Deleting field 'Topic.voted_against'
        db.delete_column(u'protocols_topic', 'voted_against')

        # Deleting field 'Topic.voted_abstain'
        db.delete_column(u'protocols_topic', 'voted_abstain')

        # Deleting field 'Topic.statement'
        db.delete_column(u'protocols_topic', 'statement')


        # Changing field 'Topic.description'
        db.alter_column(u'protocols_topic', 'description', self.gf('django.db.models.fields.TextField')(default=1))

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
            'statement': ('django.db.models.fields.TextField', [], {}),
            'voted_abstain': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'voted_against': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'voted_for': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['protocols']