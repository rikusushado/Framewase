#pragma once

#include <gtk/gtk.h>
#include <stdio.h>
#include <math.h>

#include <input/setup.h>

void slider_decoration_marks(GtkScale *slider);

static void slider_snapping(GtkScale *slider, gpointer user_data);

void slider_init(GtkBuilder *builder);