# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DetailHistory.id'
        db.delete_column(u'Lab_Electronica_detailhistory', u'id')

        # Adding field 'DetailHistory.id_history'
        db.add_column(u'Lab_Electronica_detailhistory', 'id_history',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)

        # Deleting field 'DetailCart.id'
        db.delete_column(u'Lab_Electronica_detailcart', u'id')

        # Adding field 'DetailCart.id_cart'
        db.add_column(u'Lab_Electronica_detailcart', 'id_cart',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'DetailHistory.id'
        db.add_column(u'Lab_Electronica_detailhistory', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)

        # Deleting field 'DetailHistory.id_history'
        db.delete_column(u'Lab_Electronica_detailhistory', 'id_history')

        # Adding field 'DetailCart.id'
        db.add_column(u'Lab_Electronica_detailcart', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)

        # Deleting field 'DetailCart.id_cart'
        db.delete_column(u'Lab_Electronica_detailcart', 'id_cart')


    models = {
        u'Lab_Electronica.category': {
            'Meta': {'object_name': 'Category'},
            'id_category': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'Lab_Electronica.component': {
            'Meta': {'object_name': 'Component'},
            'available': ('django.db.models.fields.IntegerField', [], {}),
            'id_category_fk': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'category'", 'to': u"orm['Lab_Electronica.Category']"}),
            'id_component': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'total': ('django.db.models.fields.IntegerField', [], {})
        },
        u'Lab_Electronica.detailcart': {
            'Meta': {'object_name': 'DetailCart'},
            'checkout': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_checkout': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id_cart': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_component_fk': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'component_cart'", 'to': u"orm['Lab_Electronica.Component']"}),
            'id_student_fk': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'student_cart'", 'to': u"orm['LabsIndex.Student']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'ready': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'Lab_Electronica.detailhistory': {
            'Meta': {'object_name': 'DetailHistory'},
            'date_in': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_out': ('django.db.models.fields.DateTimeField', [], {}),
            'id_component_fk': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'component_history'", 'to': u"orm['Lab_Electronica.Component']"}),
            'id_history': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_student_fk': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'student_history'", 'to': u"orm['LabsIndex.Student']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        u'LabsIndex.labs': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Labs'},
            'link': ('django.db.models.fields.URLField', [], {'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'})
        },
        u'LabsIndex.student': {
            'Meta': {'object_name': 'Student'},
            'career': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id_credential': ('django.db.models.fields.IntegerField', [], {'max_length': '32', 'null': 'True'}),
            'id_student': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10', 'primary_key': 'True'}),
            'labs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['LabsIndex.Labs']", 'symmetrical': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name_1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'last_name_2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['Lab_Electronica']