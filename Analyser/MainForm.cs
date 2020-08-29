using System;
using System.Collections.ObjectModel;
using System.Threading.Tasks;
using Eto.Drawing;
using Eto.Forms;

namespace Analyser
{
    public class MainForm: Form
    {
        private Command _loadCommand;
        private Command _saveCommand;
        private ObservableCollection<ClassInfo> _classes;
        public MainForm()
        {
            Title = "Adventure Analyzer";
            
            _loadCommand = new Command
            {
                MenuText = "Load",
                Enabled = true,
            };
            _loadCommand.Executed += (sender, args) => Task.Run(LoadData);
            
            _saveCommand = new Command
            {
                MenuText = "Save",
                Shortcut = Application.Instance.CommonModifier | Keys.S,
                Enabled = false,
            };
            Menu = new MenuBar
            {
                Items = { _loadCommand,  _saveCommand }
            };

            _classes = new ObservableCollection<ClassInfo>();

            var grid = new GridView();
            grid.DataStore = _classes;
            grid.Columns.Add(new GridColumn {
                DataCell = new TextBoxCell { Binding = Binding.Property<ClassInfo, string>(r => r.ID) },
                HeaderText = "ID"
            });
            grid.Columns.Add(new GridColumn {
                DataCell = new TextBoxCell { Binding = Binding.Property<ClassInfo, string>(r => r.Name) },
                HeaderText = "Name"
            });
            grid.Columns.Add(new GridColumn {
                DataCell = new CheckBoxCell { Binding = Binding.Property<ClassInfo, bool?>(r => r.IsRoom) },
                HeaderText = "Room?"
            });
            grid.Columns.Add(new GridColumn {
                DataCell = new CheckBoxCell { Binding = Binding.Property<ClassInfo, bool?>(r => r.IsItem) },
                HeaderText = "Item?"
            });

            var info = new TableLayout();
            Content = TableLayout.HorizontalScaled(grid, info);
        }

        private async void LoadData()
        {
            await Application.Instance.InvokeAsync(() => _loadCommand.Enabled = false);
            await foreach (var info in Parser.AnalyseSolution())
            {
                await Application.Instance.InvokeAsync(() => _classes.Add(info));
            }
            await Application.Instance.InvokeAsync(() => _loadCommand.Enabled = true);
        }
    }
}