#include <ui/slider_size_entry.h>

static void slider_snapping(GtkScale *slider, gpointer user_data) {
    InputOptions *config = (InputOptions *)user_data;
    
    gdouble step_size = config->slider_step_size;

    GtkRange *range = GTK_RANGE(slider); 
    gdouble free_value = gtk_range_get_value(range);
    gdouble snapped_value = round(free_value / step_size) * step_size;
    
    if (free_value != snapped_value) {
        g_signal_handlers_block_by_func(range, G_CALLBACK(slider_snapping), user_data);
        gtk_range_set_value(range, snapped_value);
        g_signal_handlers_unblock_by_func(range, G_CALLBACK(slider_snapping), user_data);
    }
}

void slider_init(GtkBuilder *builder) {
    GtkWidget *slider = GTK_WIDGET(gtk_builder_get_object(builder, "slider_size_entry"));
    
    static InputOptions setup_options = { .slider_step_size = 1.0 };
    
    g_signal_connect(slider, "value-changed", G_CALLBACK(slider_snapping), &setup_options);
}
