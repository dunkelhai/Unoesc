using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using VeterinaryClinic.BL;

namespace VeterinaryClinicWeb.Mappings
{
    public class AnimalResponsibleMap : IEntityTypeConfiguration<AnimalResponsible>
    {
        public void Configure(EntityTypeBuilder<AnimalResponsible> builder)
        {
            builder.ToTable("AnimalResponsible");

            builder.Property(p => p.Gender)
                .HasColumnType("varchar(6)")
                .HasConversion<string>();
        }
    }
}