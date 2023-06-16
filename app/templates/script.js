$(document).ready(function () {
	$("#example").DataTable({
		dom: "Bfrtip",
		buttons: [
			"copy",
			"csv",
			"excel",
			{
				text: "JSON",
				action: function (e, dt, button, config) {
					var data = dt.buttons.exportData();

					$.fn.dataTable.fileSave(
						new Blob([JSON.stringify(data)]),
						"Export.json"
					);
				},
			},
		],
	});
});
