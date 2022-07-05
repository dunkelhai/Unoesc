using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using VeterinaryClinic.BL;

namespace VeterinaryClinicWeb.Mappings
{
    public class ClinicMap : IEntityTypeConfiguration<Clinic>
    {
        public void Configure(EntityTypeBuilder<Clinic> builder)
        {
            builder.ToTable("Clinic");

            builder.Property(p => p.Name)
                .HasColumnType("varchar(100)")
                .IsRequired();

            //builder.HasData(
            //    new Clinic(1, "Au Q Mia Clínica Veterinária"));
        }
    }
}
