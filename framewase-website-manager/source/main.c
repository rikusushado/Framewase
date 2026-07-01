#include <gtk/gtk.h>

#include <ui/slider_size_entry.h>

int main(int argc, char *argv[])
{
    gtk_init(&argc, &argv);

    GtkBuilder *builder = gtk_builder_new_from_file("/home/rikusu/Documents/Programming/Framewase/framewase-website-manager/glade/window_main.glade");

    slider_init(builder);

    gtk_builder_connect_signals(builder, NULL);

    GtkWidget *window = GTK_WIDGET(gtk_builder_get_object(builder, "main_window"));
    gtk_widget_show_all(window);
    gtk_main();

    return 0;
}

