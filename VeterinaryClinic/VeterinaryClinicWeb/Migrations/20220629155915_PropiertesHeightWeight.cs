using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace VeterinaryClinicWeb.Migrations
{
    public partial class PropiertesHeightWeight : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AlterColumn<float>(
                name: "Weight",
                table: "Animal",
                type: "float(10)",
                nullable: false,
                oldClrType: typeof(decimal),
                oldType: "numeric(10,3)");

            migrationBuilder.AlterColumn<float>(
                name: "Height",
                table: "Animal",
                type: "float(5)",
                nullable: false,
                oldClrType: typeof(decimal),
                oldType: "numeric(5,2)");
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AlterColumn<decimal>(
                name: "Weight",
                table: "Animal",
                type: "numeric(10,3)",
                nullable: false,
                oldClrType: typeof(float),
                oldType: "float(10)");

            migrationBuilder.AlterColumn<decimal>(
                name: "Height",
                table: "Animal",
                type: "numeric(5,2)",
                nullable: false,
                oldClrType: typeof(float),
                oldType: "float(5)");
        }
    }
}
